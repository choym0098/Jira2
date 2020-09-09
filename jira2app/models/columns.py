# -*- coding: utf-8 -*-
import uuid

from django.db import models

from .projects import Projects


class Columns(models.Model):
    column_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    column_name = models.CharField(max_length=32, null=False)
    next_column = models.UUIDField(editable=True, null=True)

    class Meta:
        app_label = "jira2app"
