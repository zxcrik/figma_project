# Generated by Django 3.2.20 on 2023-09-22 09:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decode_blogs', '0025_auto_20230922_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 22, 15, 45, 17, 830064)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 22, 15, 45, 17, 841075)),
        ),
    ]
