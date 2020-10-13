# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Column, Project, UserProfile

admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(Column)
