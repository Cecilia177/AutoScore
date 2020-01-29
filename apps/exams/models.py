from datetime import datetime
from django.db import models
from django.utils import timezone


class Examination(models.Model):
    """
    Exam info.
    """
    exam_time = models.DateTimeField(default=datetime.now, verbose_name="考试时间（年/月）")
    exam_name = models.CharField(max_length=20, null=False, verbose_name="考试名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "考试信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.exam_name
