# Generated by Django 4.1 on 2022-08-13 02:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bracket', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['name', 'game1', 'game2']},
        ),
    ]
