from rest_framework import serializers
from .models import Student, Answer
from questions.serializers import QuestionSerializer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['text', 'score']


class StudentSerializer(serializers.ModelSerializer):
    answers = QuestionSerializer(many=True)

    class Meta:
        model = Student
        fields = ['student_sn', 'student_name', 'answers']
