# Generated by Django 3.0.2 on 2020-01-29 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20200124_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='add_time',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='add_time',
        ),
        migrations.AlterField(
            model_name='question',
            name='question_no',
            field=models.CharField(max_length=3, unique=True, verbose_name='题号'),
        ),
        migrations.AlterField(
            model_name='reference',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='refs', to='questions.Question'),
        ),
    ]
