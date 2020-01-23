from rest_framework import serializers
from .models import Examination


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examination
        fields = ['exam_time', 'exam_name', 'questions', 'students']
