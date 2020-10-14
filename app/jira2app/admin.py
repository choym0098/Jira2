# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Column, Project, UserProfile, Ticket, Comment

admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(Column)
admin.site.register(Ticket)
admin.site.register(Comment)
