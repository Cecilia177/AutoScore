# Generated by Django 3.0.2 on 2020-01-29 13:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0005_auto_20200129_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examination',
            name='exam_time',
            field=models.DateTimeField(default=datetime.date(2020, 1, 29), verbose_name='考试时间（年/月）'),
        ),
    ]
