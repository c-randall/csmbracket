# Generated by Django 4.1 on 2022-11-11 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bracket', '0031_alter_admincontrol_options_remove_series_awaytotal_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='AwayTotal',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='series',
            name='HomeTotal',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
