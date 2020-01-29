
from exams.models import Examination
from exams.serializers import ExamSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication


class ExamsListViewSet(viewsets.ModelViewSet):
    """
    List all exams.
    """
    authentication_classes = (TokenAuthentication, )
    queryset = Examination.objects.all()
    serializer_class = ExamSerializer
