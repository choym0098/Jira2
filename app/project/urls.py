# -*- coding: utf-8 -*-
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProjectViewSet

router = DefaultRouter()
router.register("projects", ProjectViewSet)

app_name = "project"

urlpatterns = [path("", include(router.urls))]
