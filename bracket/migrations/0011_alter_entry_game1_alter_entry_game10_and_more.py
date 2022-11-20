# Generated by Django 4.1 on 2022-08-17 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bracket', '0010_alter_entry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='game1',
            field=models.CharField(help_text='Winner of series 1', max_length=20),
        ),
        migrations.AlterField(
            model_name='entry',
            name='game10',
            field=models.CharField(help_text='Winner of series 10', max_length=20),
        ),
        migrations.AlterField(
            model_name='entry',
            name='game11',
            field=models.CharField(help_text='Winner of series 11', max_length=20),
        ),
        migrations.AlterField(
            model_name='entry',
            name='game12',
            field=models.CharField(help_text='Winner of series 12', max_length=20),
        ),
        migrations.AlterField(
            model_name='entry',
            name='game13',
            field=models.CharField(help_text='Winner of series 13', max_length=20),
        ),
        migrations.AlterField(
            model_name='entry',
            name='game14',
            field=models.CharField(help_text='Winner of series 14', max_length=20),
        ),
        migrations.AlterField(
            model_name='entry',
            name='game15',
            field=models.CharField(help_text='Winner of series 15', max_length=20),
        ),
        migrations.AlterField(
            model_name='entry',
            name='game2',
            field=models.CharField(help_text='Winner of series 2', max_length=20),
        ),
        migrations.AlterField(
            model_name='entry',
            name='game3',
            field=models.CharField(help_text='Winner of series 3', max_length=20),
        ),
        migrations.AlterField(
            model_name='entry',
            name='game4',
            field=models.CharField(help_text='Winner of series 4', max_length=20),
        ),
        migrations.AlterField(
            model_name='entry',
            name='game5',
            field=models.CharField(help_text='Winner of series 5', max_length=20),
        ),
        migrations.AlterField(
            model_name='entry',
            name='game6',
            field=models.CharField(help_text='Winner of series 6', max_length=20),
        ),
        migrations.AlterField(
            model_name='entry',
            name='game7',
            field=models.CharField(help_text='Winner of series 7', max_length=20),
        ),
        migrations.AlterField(
            model_name='entry',
            name='game8',
            field=models.CharField(help_text='Winner of series 8', max_length=20),
        ),
        migrations.AlterField(
            model_name='entry',
            name='game9',
            field=models.CharField(help_text='Winner of series 9', max_length=20),
        ),
        migrations.AlterField(
            model_name='masterbracket',
            name='game1',
            field=models.CharField(blank=True, help_text='Winner of series 1', max_length=20),
        ),
        migrations.AlterField(
            model_name='masterbracket',
            name='game10',
            field=models.CharField(help_text='Winner of series 10', max_length=20),
        ),
        migrations.AlterField(
            model_name='masterbracket',
            name='game11',
            field=models.CharField(help_text='Winner of series 11', max_length=20),
        ),
        migrations.AlterField(
            model_name='masterbracket',
            name='game12',
            field=models.CharField(help_text='Winner of series 12', max_length=20),
        ),
        migrations.AlterField(
            model_name='masterbracket',
            name='game13',
            field=models.CharField(help_text='Winner of series 13', max_length=20),
        ),
        migrations.AlterField(
            model_name='masterbracket',
            name='game14',
            field=models.CharField(help_text='Winner of series 14', max_length=20),
        ),
        migrations.AlterField(
            model_name='masterbracket',
            name='game15',
            field=models.CharField(blank=True, help_text='Winner of series 15', max_length=20),
        ),
        migrations.AlterField(
            model_name='masterbracket',
            name='game2',
            field=models.CharField(help_text='Winner of series 2', max_length=20),
        ),
        migrations.AlterField(
            model_name='masterbracket',
            name='game3',
            field=models.CharField(help_text='Winner of series 3', max_length=20),
        ),
        migrations.AlterField(
            model_name='masterbracket',
            name='game4',
            field=models.CharField(help_text='Winner of series 4', max_length=20),
        ),
        migrations.AlterField(
            model_name='masterbracket',
            name='game5',
            field=models.CharField(help_text='Winner of series 5', max_length=20),
        ),
        migrations.AlterField(
            model_name='masterbracket',
            name='game6',
            field=models.CharField(help_text='Winner of series 6', max_length=20),
        ),
        migrations.AlterField(
            model_name='masterbracket',
            name='game7',
            field=models.CharField(help_text='Winner of series 7', max_length=20),
        ),
        migrations.AlterField(
            model_name='masterbracket',
            name='game8',
            field=models.CharField(help_text='Winner of series 8', max_length=20),
        ),
        migrations.AlterField(
            model_name='masterbracket',
            name='game9',
            field=models.CharField(help_text='Winner of series 9', max_length=20),
        ),
    ]