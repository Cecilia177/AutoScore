from rest_framework import serializers
from .models import Student, Answer
from questions.serializers import ExamSerializerOfName, QuestionSerializerOfName


class StudentSerializerOfName(serializers.ModelSerializer):
    exam = ExamSerializerOfName()

    class Meta:
        model = Student
        fields = ['student_sn', 'student_name', 'exam']


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 'student_sn', 'student_name', 'exam']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['text', 'score', 'question', 'student']


class AnswerDetailSerializer(serializers.ModelSerializer):
    student = StudentSerializerOfName()
    question = QuestionSerializerOfName()

    class Meta:
        model = Answer
        fields = ['id', 'text', 'score', 'question', 'student']


class StudentDetailSerializer(serializers.ModelSerializer):
    exam = ExamSerializerOfName()
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'student_sn', 'student_name', 'exam', 'answers']


class StudentScoresSerializer(serializers.ModelSerializer):
    exam = ExamSerializerOfName()
    answers = AnswerDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'student_sn', 'student_name', 'exam', 'answers']
