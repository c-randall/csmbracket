# Generated by Django 4.1 on 2022-12-02 01:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bracket', '0048_delete_masterbracket_alter_blogpost_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='series',
            name='isMatchupSet',
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 1, 18, 48, 25, 173894), null=True),
        ),
    ]
