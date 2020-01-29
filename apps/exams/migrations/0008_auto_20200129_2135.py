# Generated by Django 3.0.2 on 2020-01-29 13:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0007_auto_20200129_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examination',
            name='exam_time',
            field=models.DateTimeField(default=django.utils.timezone.localdate, verbose_name='考试时间（年/月）'),
        ),
    ]