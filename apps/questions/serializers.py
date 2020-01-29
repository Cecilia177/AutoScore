from rest_framework import serializers
from .models import Question, Reference


class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = ['language', 'text', 'question']


class QuestionSerializer(serializers.ModelSerializer):
    refs = ReferenceSerializer(many=True, allow_null=True, read_only=True)

    class Meta:
        model = Question
        fields = "__all__"

