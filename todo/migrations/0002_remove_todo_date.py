# Generated by Django 3.0.5 on 2020-06-26 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='date',
        ),
    ]
