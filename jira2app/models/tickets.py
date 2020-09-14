# -*- coding: utf-8 -*-
import uuid

from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models

from jira2app.models import Columns


class Tickets(models.Model):
    ticket_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    column = models.ForeignKey(Columns, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now=True, null=False)
    modified_time = models.DateTimeField(auto_now_add=True, null=False)
    ticket_description = models.TextField(null=True, editable=True)
    ticket_title = models.CharField(max_length=64, null=False, editable=True)
    followers = ArrayField(models.UUIDField(editable=True), blank=True, editable=True)

    class Meta:
        app_label = "jira2app"
