# Generated by Django 4.1.5 on 2023-01-14 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("baseapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="answer",
            name="answer_text",
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name="question",
            name="question_text",
            field=models.JSONField(),
        ),
    ]
