from datetime import datetime
from django.db import models

# Create your models here.


class Student(models.Model):
    """
    Student information.
    """
    student_sn = models.CharField(max_length=30, null=False, verbose_name="学生考号")
    student_name = models.CharField(max_length=10, default="", verbose_name="学生姓名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "学生信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.student_sn



