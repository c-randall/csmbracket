# Generated by Django 4.1 on 2022-08-13 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bracket', '0003_alter_entry_options_entry_participating'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]