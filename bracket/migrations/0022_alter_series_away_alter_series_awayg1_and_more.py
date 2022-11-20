# Generated by Django 4.1 on 2022-11-10 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bracket', '0021_rename_series_num_series_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='Away',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='series',
            name='AwayG1',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='AwayG2',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='AwayG3',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='AwayG4',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='AwayG5',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='AwayG6',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='AwayG7',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='HomeG1',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='HomeG2',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='HomeG3',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='HomeG4',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='HomeG5',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='HomeG6',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='HomeG7',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='num',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
