import django_filters
from .models import Examination


class ExamFilter(django_filters.rest_framework.FilterSet):
    exam_name = django_filters.CharFilter(field_name='exam_name', lookup_expr='icontains')

    class Meta:
        model = Examination
        fields = ['exam_name']
