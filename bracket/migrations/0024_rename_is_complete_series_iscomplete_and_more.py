# Generated by Django 4.1 on 2022-11-10 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bracket', '0023_series_is_complete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='series',
            old_name='is_complete',
            new_name='IsComplete',
        ),
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
