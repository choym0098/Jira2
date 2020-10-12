from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProjectViewSet


router = DefaultRouter()
router.register('projects', ProjectViewSet)

app_name = 'project'

urlpatterns = [
    path('', include(router.urls))
]
