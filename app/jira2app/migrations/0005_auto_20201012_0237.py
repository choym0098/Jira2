# -*- coding: utf-8 -*-
# Generated by Django 2.1.15 on 2020-10-12 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jira2app", "0004_auto_20201012_0237"),
    ]

    operations = [
        migrations.AlterField(
            model_name="column",
            name="next_column",
            field=models.ManyToManyField(
                blank=True, related_name="_column_next_column_+", to="jira2app.Column"
            ),
        ),
    ]
