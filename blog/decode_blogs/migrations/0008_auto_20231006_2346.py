# Generated by Django 3.2.20 on 2023-10-06 17:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decode_blogs', '0007_auto_20231006_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 6, 23, 45, 58, 759995)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 6, 23, 45, 58, 760996)),
        ),
    ]