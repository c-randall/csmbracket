# Generated by Django 4.1 on 2022-11-10 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bracket', '0028_startingteam_delete_startingteams'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='startingteam',
            name='initialize_series',
        ),
        migrations.AlterField(
            model_name='masterbracket',
            name='series1',
            field=models.CharField(blank=True, help_text='Winner of series 1', max_length=12),
        ),
        migrations.AlterField(
            model_name='masterbracket',
            name='series10',
            field=models.CharField(blank=True, help_text='Winner of series 10', max_length=12),
        ),
        migrations.AlterField(
            model_name='masterbracket',
            name='series11',
            field=models.CharField(blank=True, help_text='Winner of series 11', max_length=12),
        ),
        migrations.AlterField(
            model_name='masterbracket',
            name='series12',
            field=models.CharField(blank=True, help_text='Winner of series 12', max_length=12),
        ),
        migrations.AlterField(
            model_name='masterbracket',
            name='series13',
            field=models.CharField(blank=True, help_text='Winner of series 13', max_length=12),
        ),
        migrations.AlterField(
            model_name='masterbracket',
            name='series14',
            field=models.CharField(blank=True, help_text='Winner of series 14', max_length=12),
        ),
        migrations.AlterField(
            model_name='masterbracket',
            name='series15',
            field=models.CharField(blank=True, help_text='Winner of series 15', max_length=12),
        ),
        migrations.AlterField(
            model_name='masterbracket',
            name='series2',
            field=models.CharField(blank=True, help_text='Winner of series 2', max_length=12),
        ),
        migrations.AlterField(
            model_name='masterbracket',
            name='series3',
            field=models.CharField(blank=True, help_text='Winner of series 3', max_length=12),
        ),
        migrations.AlterField(
            model_name='masterbracket',
            name='series4',
            field=models.CharField(blank=True, help_text='Winner of series 4', max_length=12),
        ),
        migrations.AlterField(
            model_name='masterbracket',
            name='series5',
            field=models.CharField(blank=True, help_text='Winner of series 5', max_length=12),
        ),
        migrations.AlterField(
            model_name='masterbracket',
            name='series6',
            field=models.CharField(blank=True, help_text='Winner of series 6', max_length=12),
        ),
        migrations.AlterField(
            model_name='masterbracket',
            name='series7',
            field=models.CharField(blank=True, help_text='Winner of series 7', max_length=12),
        ),
        migrations.AlterField(
            model_name='masterbracket',
            name='series8',
            field=models.CharField(blank=True, help_text='Winner of series 8', max_length=12),
        ),
        migrations.AlterField(
            model_name='masterbracket',
            name='series9',
            field=models.CharField(blank=True, help_text='Winner of series 9', max_length=12),
        ),
        migrations.AlterField(
            model_name='series',
            name='Away',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='series',
            name='Home',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]