from datetime import datetime
from rest_framework import serializers
from .models import Question


class ExamSerializer(serializers.Serializer):
    exam_time = serializers.DateTimeField(default=datetime.now)
    exam_name = serializers.CharField(max_length=20, default="第一次考试")
