# Generated by Django 4.1 on 2022-11-11 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bracket', '0030_alter_entry_series1_alter_entry_series10_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='admincontrol',
            options={'verbose_name': 'Admin Control', 'verbose_name_plural': 'Admin Controls'},
        ),
        migrations.RemoveField(
            model_name='series',
            name='AwayTotal',
        ),
        migrations.RemoveField(
            model_name='series',
            name='HomeTotal',
        ),
    ]
