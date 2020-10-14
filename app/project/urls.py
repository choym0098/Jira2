# -*- coding: utf-8 -*-
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProjectViewSet, TicketViewSet

router = DefaultRouter()
router.register("projects", ProjectViewSet)
router.register("tickets", TicketViewSet)

app_name = "project"

urlpatterns = [path("", include(router.urls))]
