# Generated by Django 3.1.3 on 2020-11-26 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultation',
            name='endtime',
        ),
        migrations.RemoveField(
            model_name='consultation',
            name='startime',
        ),
        migrations.AddField(
            model_name='consultation',
            name='gmeet_link',
            field=models.TextField(null=True),
        ),
    ]
