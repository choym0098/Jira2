# -*- coding: utf-8 -*-
from django.db import models


class Label(models.Model):
    label_name = models.CharField(max_length=255, null=False)
    label_colour = models.CharField(max_length=255, null=False)

    class Meta:
        app_label = "jira2app"
