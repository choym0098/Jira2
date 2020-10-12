from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import ProjectSerializer
from jira2app.models import Project


class ProjectViewSet(viewsets.ModelViewSet):
    """Manage projects in the database"""
    queryset = Project.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectSerializer
