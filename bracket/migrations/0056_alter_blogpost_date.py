# Generated by Django 4.1 on 2023-04-18 16:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bracket', '0055_alter_blogpost_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 18, 10, 10, 4, 11289), null=True),
        ),
    ]
