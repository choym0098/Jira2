# Generated by Django 2.1.15 on 2020-10-12 03:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jira2app', '0005_auto_20201012_0237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='column',
            name='next_column',
        ),
    ]
