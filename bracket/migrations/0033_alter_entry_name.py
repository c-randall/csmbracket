# Generated by Django 4.1 on 2022-11-11 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bracket', '0032_series_awaytotal_series_hometotal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
