from datetime import datetime
from django.db import models
from django.utils.timezone import timezone
from exams.models import Examination
# Create your models here.


class Question(models.Model):
    """
    Question info.
    """
    QUESTION_TYPE = (
        (1, "填空题"),
        (2, "改错题"),
        (3, "翻译题"),
        (4, "简答题")
    )
    question_no = models.CharField(unique=True, max_length=3, null=False, verbose_name="题号")
    question_type = models.IntegerField(default=1, choices=QUESTION_TYPE, verbose_name="问题类型",
                                        help_text="问题类型：1(填空),2(改错),3(翻译),4(简答)")
    full_score = models.FloatField(max_length=3, null=False, verbose_name="满分值")
    # add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    exam = models.ForeignKey(Examination, null=True, blank=True, on_delete=models.CASCADE, related_name="questions")

    class Meta:
        verbose_name = "题目信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question_no


class Reference(models.Model):
    """
    Reference info.
    """
    LANGUAGE_CHOICES = (
        (1, "英文"),
        (2, "中文")
    )
    language = models.IntegerField(default=1, choices=LANGUAGE_CHOICES, verbose_name="语言类型")
    text = models.TextField(max_length=200, default="", verbose_name="文本内容")
    # add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    question = models.ForeignKey(Question, null=True, related_name="refs", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "参考答案"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text
