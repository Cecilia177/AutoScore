
from exams.models import Examination
from exams.serializers import ExamSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from exams.filters import ExamFilter


class ExamsListViewSet(viewsets.ModelViewSet):
    """
    List all exams.
    """
    authentication_classes = (TokenAuthentication, )
    queryset = Examination.objects.all()
    serializer_class = ExamSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = ExamFilter
    search_fields = ['exam_name']
    pagination_class = None
