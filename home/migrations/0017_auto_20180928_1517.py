# Generated by Django 2.1 on 2018-09-28 15:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20180928_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 28, 15, 17, 56, 76516, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 28, 15, 17, 56, 75067, tzinfo=utc)),
        ),
    ]