# Generated by Django 4.1 on 2022-11-11 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bracket', '0033_alter_entry_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(blank=True, null=True)),
                ('message', models.CharField(max_length=5000)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name': 'Entry', 'verbose_name_plural': 'Entries'},
        ),
        migrations.AlterModelOptions(
            name='masterbracket',
            options={'verbose_name': 'Master', 'verbose_name_plural': 'Master'},
        ),
        migrations.AlterModelOptions(
            name='startingteam',
            options={'ordering': ('Index',), 'verbose_name': 'Starting Team', 'verbose_name_plural': 'Starting Teams'},
        ),
    ]