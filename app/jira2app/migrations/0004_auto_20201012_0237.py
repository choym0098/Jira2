# -*- coding: utf-8 -*-
# Generated by Django 2.1.15 on 2020-10-12 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jira2app", "0003_auto_20201012_0232"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="column",
            name="next_column",
        ),
        migrations.AddField(
            model_name="column",
            name="next_column",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="_column_next_column_+",
                to="jira2app.Column",
            ),
        ),
    ]
