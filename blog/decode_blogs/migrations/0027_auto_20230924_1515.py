# Generated by Django 3.2.20 on 2023-09-24 09:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decode_blogs', '0026_auto_20230922_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 24, 15, 14, 58, 151540)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 24, 15, 14, 58, 152539)),
        ),
    ]
