# Generated by Django 3.2.20 on 2023-09-09 17:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decode_blogs', '0012_auto_20230909_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 9, 23, 10, 57, 773165)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 9, 23, 10, 57, 774165)),
        ),
    ]
