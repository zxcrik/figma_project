# Generated by Django 3.2.20 on 2023-09-12 11:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decode_blogs', '0014_auto_20230910_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 12, 17, 11, 50, 199031)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 12, 17, 11, 50, 215092)),
        ),
    ]