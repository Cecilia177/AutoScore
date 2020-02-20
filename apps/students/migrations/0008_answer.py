# Generated by Django 3.0.2 on 2020-02-20 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_auto_20200201_1706'),
        ('students', '0007_delete_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='', max_length=200, verbose_name='回答内容')),
                ('score', models.FloatField(default=-1.0, max_length=3, verbose_name='得分')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Question')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='students.Student')),
            ],
            options={
                'verbose_name': '学生回答',
                'verbose_name_plural': '学生回答',
                'unique_together': {('student', 'question')},
            },
        ),
    ]