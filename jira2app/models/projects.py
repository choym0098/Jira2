# -*- coding: utf-8 -*-
import uuid

from django.contrib.auth.models import User
from django.db import models


class Projects(models.Model):
    project_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project_name = models.CharField(max_length=32, null=False)
    project_description = models.TextField()
    is_private = models.BooleanField(default=True, null=False)
    created_time = models.DateTimeField(auto_now_add=True, null=False)
    modified_time = models.DateTimeField(auto_now=True, null=False)
    user = models.ManyToManyField(User, null=False)

    class Meta:
        app_label = "jira2app"
