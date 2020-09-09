# -*- coding: utf-8 -*-
import uuid

from django.db import models


class Projects(models.Model):
    projectId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    projectName = models.CharField(max_length=32, null=False)
    projectDescription = models.TextField()
    isPrivate = models.BooleanField(default=True, null=False)
    createdTime = models.DateTimeField(auto_now_add=True, null=False)
    modifiedTime = models.DateTimeField(auto_now=True, null=False)

    # TODO: add foregin key after creating Users table
    # userId = models.

    class Meta:
        app_label = "jira2app"
