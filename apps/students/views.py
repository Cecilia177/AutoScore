import math
from joblib import load

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins
from stanfordcorenlp import StanfordCoreNLP
from gensim.models import KeyedVectors

from students.models import Student, Answer
from questions.models import Question
from students.serializers import StudentSerializer, AnswerDetailSerializer, AnswerSerializer, \
    StudentDetailSerializer, StudentScoresSerializer

from db_tools.features import cal_features


class StudentViewSet(viewsets.ModelViewSet):
    """
    List all exams.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_fields = ['exam', 'student_sn']
    search_fields = ['student_name', 'student_sn']

    def get_serializer_class(self):
        print(self.action)
        if self.action == 'update' or self.action == 'create' or self.action == 'retrieve':
            return StudentSerializer
        return StudentDetailSerializer


class ScoresViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentScoresSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['exam']
    pagination_class = None


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()

    def get_serializer_class(self):
        if self.action == 'update' or self.action == 'create' or self.action == 'retrieve':
            return AnswerSerializer
        return AnswerDetailSerializer


class ScoringViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    queryset = Answer.objects.all()
    pagination_class = None

    def get_serializer_class(self):
        if self.action == 'update' or self.action == 'create' or self.action == 'retrieve':
            return AnswerSerializer
        return AnswerDetailSerializer

    def get_queryset(self):
        return self.scoring()

    # 评分逻辑
    def scoring(self):
        queryset = self.queryset
        # 参考答案与作答集合
        # refs = {}  # key is question id and value is a list of references of the question
        # answers = {}  # key is question id and value is a list of the answers of the question
        # answer_ids = {}  # key is question id and value is a list of the answers ids
        # ques_type = {}
        #
        # for answer in queryset:
        #     current_question = answer.question
        #     if current_question.question_type == 3 or current_question.question_type == 4:
        #         if current_question.id not in ques_type.keys():
        #             ques_type[current_question.id] = current_question.question_type
        #         if current_question.id not in refs.keys():
        #             refs[current_question.id] = answer.question.refs.split("/")
        #         if current_question.id not in answers.keys():
        #             answers[current_question.id] = [answer.text]
        #         else:
        #             answer[current_question.id].append(answer.text)
        #         if current_question.id not in answer_ids.keys():
        #             answer_ids[current_question.id] = [answer.id]
        #         else:
        #             answer_ids[current_question.id].append(answer.id)

        # 逐个题目进行评分
        questions = Question.objects.all()

        # zh_word_vectors = KeyedVectors.load("apps/db_tools/model/vectors.kv")
        # zh_model = StanfordCoreNLP("apps/db_tools/model/stanford-corenlp-full-2018-02-27", lang='zh')
        en_word_vectors = KeyedVectors.load("apps/db_tools/model/vectors_en.kv")
        en_model = StanfordCoreNLP("apps/db_tools/model/stanford-corenlp-full-2018-02-27")
        for ques in questions:
            answers = queryset.filter(question=ques.id)
            refs = ques.refs
            answers_text = [answer.text for answer in answers]
            refs_text = refs.split("/")
            answers_ids = [answer.id for answer in answers]
            print(answers_ids)
            if ques.question_type == 1 or ques.question_type == 2:  # 填空题或改错题
                for answer in answers:
                    if answer.text in refs:
                        answer.score = ques.full_score
                    else:
                        answer.score = 0
                    answer.save()
            # elif ques.question_type == 3:
            #     features = cal_features(refs=refs_text, answers=answers_text, answer_ids=answers_ids,
            #                             question_type=3, word2vec_model=zh_word_vectors, nlp_model=zh_model)
            elif ques.question_type == 4:
                features_list = cal_features(refs=refs_text, answers=answers_text, answer_ids=answers_ids,
                                             question_type=4, word2vec_model=en_word_vectors, nlp_model=en_model)
            if ques.question_type == 3 or ques.question_type == 4:
                model_path = "apps/db_tools/model/scoring_model_en.joblib" if ques.question_type == 4 \
                    else "apps/db_tools/model/scoring_model_ch.joblib"
                scoring_model = load(model_path)
                for answer in answers:
                    score = scoring_model.predict([features_list[answer.id]])[0] * ques.full_score / 2
                    print("predict:", score)
                    decimal = score - math.floor(score)
                    integral = score - decimal
                    print("dec:", decimal, " int:", integral)
                    if score < 0:
                        answer.score = 0
                    elif 0 <= decimal < 0.25:
                        answer.score = integral
                    elif 0.25 <= decimal < 0.75:
                        answer.score = integral + 0.5
                    else:
                        answer.score = integral + 1
                    answer.save()

        # features_list = {}
        # for ques in refs.keys():
        #     if ques_type[ques] == 3:
        #         features = cal_features(refs=refs[ques], answers=answers[ques], answer_ids=answer_ids[ques],
        #                                 question_type=3, word2vec_model=zh_word_vectors, nlp_model=zh_model)
        #     elif ques_type[ques] == 4:
        #         features = cal_features(refs=refs[ques], answers=answers[ques], answer_ids=answer_ids[ques],
        #                                 question_type=4, word2vec_model=en_word_vectors, nlp_model=en_model)
        #     features_list[ques] = features
        # for answer in queryset:
        #     question_type = answer.question.question_type
        #     full_score = answer.question.full_score
        #     refs = answer.question.refs.split("/")
        #     text = answer.text
        #     answer.score = 0
        #     print(answer.text + ":" + str(question_type))
        #     if question_type == 1:  # 填空题
        #         if text in refs:
        #             answer.score = full_score
        #         answer.score = 10
        #     elif question_type == 2:  # 改错题
        #         if text in refs:
        #             answer.score = full_score
        #     elif question_type == 3:  # 翻译题
        #         print("翻译题")
        #         print(features_list[answer.question.id][answer.id])
        #     elif question_type == 4:
        #         print("简答")
        #         print(features_list[answer.question.id][answer.id])
        #     answer.save()
        return queryset




