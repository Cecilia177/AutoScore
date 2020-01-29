from rest_framework import serializers
from .models import Examination
from questions.serializers import QuestionSerializer


class ExamSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, allow_null=True, read_only=True)

    class Meta:
        model = Examination
        fields = ['id', 'exam_time', 'exam_name', 'questions']
