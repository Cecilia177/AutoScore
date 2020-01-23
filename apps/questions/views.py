
from questions.models import Question, Reference
from questions.serializers import QuestionSerializer, ReferenceSerializer
from rest_framework import viewsets


class QuestionsViewSet(viewsets.ModelViewSet):
    """
    List all exams.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ReferenceViewSet(viewsets.ModelViewSet):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer
