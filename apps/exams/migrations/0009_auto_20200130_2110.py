# Generated by Django 3.0.2 on 2020-01-30 13:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0008_auto_20200129_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examination',
            name='exam_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='考试时间（年/月）'),
        ),
    ]
