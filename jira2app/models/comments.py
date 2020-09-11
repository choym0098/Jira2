# -*- coding: utf-8 -*-
import uuid

from django.db import models

from jira2app.models import Tickets


class Comments(models.Model):
    comment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ticket = models.ForeignKey(Tickets, on_delete=models.CASCADE)
    user = models.ForeignKey("Users", on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now=True, null=False)
    modified_time = models.DateTimeField(auto_now_add=True, null=False)
    message = models.TextField(null=False, editable=True)

    class Meta:
        app_label = "jira2app"
