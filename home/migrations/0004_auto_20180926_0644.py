# Generated by Django 2.1 on 2018-09-26 06:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20180926_0636'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 26, 6, 44, 53, 118471, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='question',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 26, 6, 44, 53, 117570, tzinfo=utc)),
        ),
    ]