# Generated by Django 4.1 on 2022-08-14 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bracket', '0007_masterbracket'),
    ]

    operations = [
        migrations.CreateModel(
            name='StartingTeams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team1', models.CharField(max_length=20)),
                ('team2', models.CharField(max_length=20)),
                ('team3', models.CharField(max_length=20)),
                ('team4', models.CharField(max_length=20)),
                ('team5', models.CharField(max_length=20)),
                ('team6', models.CharField(max_length=20)),
                ('team7', models.CharField(max_length=20)),
                ('team8', models.CharField(max_length=20)),
                ('team9', models.CharField(max_length=20)),
                ('team10', models.CharField(max_length=20)),
                ('team11', models.CharField(max_length=20)),
                ('team12', models.CharField(max_length=20)),
                ('team13', models.CharField(max_length=20)),
                ('team14', models.CharField(max_length=20)),
                ('team15', models.CharField(max_length=20)),
                ('team16', models.CharField(max_length=20)),
            ],
        ),
    ]