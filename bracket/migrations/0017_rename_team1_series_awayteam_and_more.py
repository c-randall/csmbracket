# Generated by Django 4.1 on 2022-11-10 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bracket', '0016_rename_still_open_controlform_activate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='series',
            old_name='team1',
            new_name='AwayTeam',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='team2',
            new_name='HomeTeam',
        ),
        migrations.RemoveField(
            model_name='series',
            name='g1_date',
        ),
        migrations.RemoveField(
            model_name='series',
            name='g2_date',
        ),
        migrations.RemoveField(
            model_name='series',
            name='g3_date',
        ),
        migrations.RemoveField(
            model_name='series',
            name='g4_date',
        ),
        migrations.RemoveField(
            model_name='series',
            name='g5_date',
        ),
        migrations.RemoveField(
            model_name='series',
            name='g6_date',
        ),
        migrations.RemoveField(
            model_name='series',
            name='g7_date',
        ),
    ]
