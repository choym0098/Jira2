# -*- coding: utf-8 -*-
from django.urls import path

from . import views

app_name = "jira2app"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
]
