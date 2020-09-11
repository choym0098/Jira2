# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

from jira2app.models import Projects


class UsersProjects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, null=True)

    class Meta:
        app_label = "jira2app"
