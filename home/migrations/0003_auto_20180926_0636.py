# Generated by Django 2.1 on 2018-09-26 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_question_interests'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='downvote',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='answer',
            name='upvote',
            field=models.IntegerField(default=0),
        ),
    ]