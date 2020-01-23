
from exams.models import Examination
from exams.serializers import ExamSerializer
from rest_framework import viewsets


class ExamsListViewSet(viewsets.ModelViewSet):
    """
    List all exams.
    """
    queryset = Examination.objects.all()
    serializer_class = ExamSerializer
