# Generated by Django 3.0.2 on 2020-01-24 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0002_auto_20200124_1629'),
        ('students', '0002_auto_20200123_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='answers',
        ),
        migrations.AddField(
            model_name='answer',
            name='score',
            field=models.FloatField(default=0.0, max_length=3, verbose_name='得分'),
        ),
        migrations.AddField(
            model_name='answer',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='students.Student'),
        ),
        migrations.AddField(
            model_name='student',
            name='exam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='exams.Examination'),
        ),
    ]
