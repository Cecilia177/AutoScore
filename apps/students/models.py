from datetime import datetime
from django.db import models
from questions.models import Question
from exams.models import Examination


class Student(models.Model):
    """
    Student information.
    """
    student_sn = models.CharField(max_length=30, null=False, verbose_name="学生考号")
    student_name = models.CharField(max_length=10, default="", verbose_name="学生姓名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    exam = models.ForeignKey(Examination, blank=True, null=True, on_delete=models.CASCADE, related_name="students")

    class Meta:
        verbose_name = "学生信息"
        verbose_name_plural = verbose_name
        unique_together = ("student_sn", "exam")

    def __str__(self):
        return self.student_name + " " + self.student_sn


class Answer(models.Model):
    """
    Answer info.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField(max_length=200, default="", verbose_name="回答内容")
    student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.CASCADE, related_name="answers")
    score = models.FloatField(max_length=3, default=-1.0, verbose_name="得分")

    class Meta:
        verbose_name = "学生回答"
        verbose_name_plural = verbose_name
        unique_together = ('student', 'question')

    def __str__(self):
        return self.text





