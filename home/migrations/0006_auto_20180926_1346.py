# Generated by Django 2.1 on 2018-09-26 13:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20180926_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 26, 13, 46, 4, 416969, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 26, 13, 46, 4, 416234, tzinfo=utc)),
        ),
    ]
