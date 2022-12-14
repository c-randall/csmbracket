# Generated by Django 4.1 on 2022-11-12 17:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bracket', '0037_alter_blogpost_options_alter_series_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='points',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='entry',
            name='tpp',
            field=models.PositiveSmallIntegerField(default=380),
        ),
        migrations.AddField(
            model_name='masterbracket',
            name='points',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='masterbracket',
            name='tpp',
            field=models.PositiveSmallIntegerField(default=380),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 12, 10, 34, 44, 456741), null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(upload_to='bracket/static/images/BlogPosts'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
