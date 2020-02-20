
from questions.models import Question
from questions.serializers import QuestionSerializer, QuestionDetailSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


class QuestionsViewSet(viewsets.ModelViewSet):
    """
    List all exams.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['exam', 'question_type', 'question_no']

    def get_serializer_class(self):
        print(self.action)
        if self.action == 'update' or self.action == 'create' or self.action == 'retrieve':
            return QuestionSerializer
        return QuestionDetailSerializer


# class ReferenceViewSet(viewsets.ModelViewSet):
#     queryset = Reference.objects.all()
#     serializer_class = ReferenceSerializer
