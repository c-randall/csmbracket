# Generated by Django 4.1 on 2023-04-17 15:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bracket', '0051_rename_resetall_admincontrol_initialize_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 17, 9, 4, 24, 927893), null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, upload_to='BlogPosts'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='series1',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='entry',
            name='series10',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='entry',
            name='series11',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='entry',
            name='series12',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='entry',
            name='series13',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='entry',
            name='series14',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='entry',
            name='series15',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='entry',
            name='series2',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='entry',
            name='series3',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='entry',
            name='series4',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='entry',
            name='series5',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='entry',
            name='series6',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='entry',
            name='series7',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='entry',
            name='series8',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='entry',
            name='series9',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='series',
            name='Away',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='series',
            name='Home',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='series',
            name='Loser',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='series',
            name='Winner',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='startingteam',
            name='Name',
            field=models.CharField(max_length=20),
        ),
    ]
