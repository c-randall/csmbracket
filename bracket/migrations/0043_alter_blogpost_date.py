# Generated by Django 4.1 on 2022-11-20 18:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bracket', '0042_delete_rounddates_alter_blogpost_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 20, 11, 16, 43, 731180), null=True),
        ),
    ]
