from datetime import datetime
from django.db import models
from exams.models import Examination, Question
from students.models import Student
# Create your models here.


class Score(models.Model):
    """
    Score info.
    """
    exam = models.ForeignKey(Examination, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    score = models.FloatField(default=0, verbose_name="分数值")

    class Meta:
        verbose_name = "分数信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.score
