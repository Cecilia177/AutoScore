from rest_framework import serializers
from .models import Question
from exams.models import Examination
# from exams.serializers import ExamSerializer


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = "__all__"


class ExamSerializerOfName(serializers.ModelSerializer):
    class Meta:
        model = Examination
        fields = ['exam_name']


class QuestionDetailSerializer(serializers.ModelSerializer):
    exam = ExamSerializerOfName()
    # answers = QuestionSerializer(many=True, allow_null=True, read_only=True)

    class Meta:
        model = Question
        fields = "__all__"


class QuestionSerializerOfName(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question_no', 'question_type', 'refs', 'full_score']




