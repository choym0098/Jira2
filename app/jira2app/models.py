# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import ArrayField


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f"user_{instance.user.id}/{filename}"


class TimeStampMixin(models.Model):
    """Abstract class to be used in models with timestamps"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserProfile(models.Model):
    """User Profile to contain user's profile photo"""

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to=user_directory_path)


class Project(TimeStampMixin):
    """Project model"""

    project_name = models.CharField(max_length=32, blank=False)
    project_description = models.TextField()
    is_private = models.BooleanField(default=True)
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name="projects"
    )


class Column(models.Model):
    """Column to be used in project model"""

    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="columns"
    )
    column_name = models.CharField(max_length=32, blank=True)
    next_column = models.ManyToManyField("self", blank=True, editable=True)


class Ticket(TimeStampMixin):
    """Ticket to be used in column model"""
    column = models.ForeignKey(
        Column, on_delete=models.CASCADE, related_name='tickets'
    )
    ticket_title = models.CharField(max_length=32, null=False)
    ticket_description = models.TextField()
    notifyees = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name='tickets'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False,
    )
