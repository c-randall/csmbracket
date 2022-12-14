# Generated by Django 4.1 on 2022-08-13 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter a participant's name", max_length=200)),
                ('game1', models.CharField(help_text='Enter the winner of game 1', max_length=20)),
                ('game2', models.CharField(help_text='Enter the winner of game 2', max_length=20)),
                ('game3', models.CharField(help_text='Enter the winner of game 3', max_length=20)),
                ('game4', models.CharField(help_text='Enter the winner of game 4', max_length=20)),
                ('game5', models.CharField(help_text='Enter the winner of game 5', max_length=20)),
                ('game6', models.CharField(help_text='Enter the winner of game 6', max_length=20)),
                ('game7', models.CharField(help_text='Enter the winner of game 7', max_length=20)),
                ('game8', models.CharField(help_text='Enter the winner of game 8', max_length=20)),
                ('game9', models.CharField(help_text='Enter the winner of game 9', max_length=20)),
                ('game10', models.CharField(help_text='Enter the winner of game 10', max_length=20)),
                ('game11', models.CharField(help_text='Enter the winner of game 11', max_length=20)),
                ('game12', models.CharField(help_text='Enter the winner of game 12', max_length=20)),
                ('game13', models.CharField(help_text='Enter the winner of game 13', max_length=20)),
                ('game14', models.CharField(help_text='Enter the winner of game 14', max_length=20)),
                ('game15', models.CharField(help_text='Enter the winner of game 15', max_length=20)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
