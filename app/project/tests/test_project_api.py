from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from jira2app.models import Project

from project.serializers import ProjectSerializer

# default router for project api
PROJECTS_URL = reverse('project:project-list')


class PublicProjectApiTests(TestCase):
    """Test the publicly available projects API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required to access the endpoint"""
        res = self.client.get(PROJECTS_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateProjectsAPITests(TestCase):
    """Test the private projects API"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'Test',
            'test123'
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_project_list(self):
        """Test retrieving a list of projects"""
        project1 = Project.objects.create(
            project_name='test 1',
            project_description='description 1',
        )
        project2 = Project.objects.create(
            project_name='test 2',
            project_description='description 2',
        )
        project1.users.add(self.user)
        project2.users.add(self.user)

        res = self.client.get(PROJECTS_URL)

        projects = Project.objects.all().order_by('-project_name')
        serializer = ProjectSerializer(projects, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_projects_limited_to_user(self):
        """Test that ingredients for the authenticate user are returned"""
        user2 = get_user_model().objects.create_user(
            'test2',
            'test123'
        )

        project = Project.objects.create(
            project_name='test 1',
            project_description='description 1',
        )
        project2 = Project.objects.create(
            project_name='test 2',
            project_description='description 2',
        )
        project.users.add(self.user)
        project2.users.add(user2)

        res = self.client.get(PROJECTS_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['project_name'], project.project_name)
