from django.contrib.auth import get_user_model
from django.test import TestCase

from jira2app import models


def sample_user(username='test', password='test123'):
    """Create a sample user"""
    return get_user_model().objects.create_user(username, password)


def sample_project(project_name='Test project name', project_description='Test project description'):
    return models.Project.objects.create(
        project_name=project_name,
        project_description=project_description
    )


def sample_column(column_name='Test column name'):
    return models.Column.objects.create(
        project=sample_project(),
        column_name=column_name
    )


def sample_ticket(ticket_title='Test ticket title', ticket_description='Test ticket description'):
    return models.Ticket.objects.create(
        column=sample_column(),
        ticket_title=ticket_title,
        ticket_description=ticket_description,
        user=sample_user()
    )


class ModelTests(TestCase):
    """Test basic object creation with string representtaion"""

    def test_create_user_successful(self):
        """Test creating a new user is successful"""
        username = 'test'
        password = 'test123'
        user = get_user_model().objects.create_user(
            username=username,
            password=password
        )

        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))

    def test_create_project_str(self):
        """Test the project string representation"""
        project = models.Project.objects.create(
            project_name='Test project name',
            project_description='Test project description'
        )

        self.assertEqual(str(project), project.project_name)

    def test_create_column_str(self):
        """Test the project string representation"""
        column = models.Column.objects.create(
            project=sample_project(),
            column_name='Test column name',
        )

        self.assertEqual(str(column), column.column_name)

    def test_create_ticket_str(self):
        """Test the project string representation"""
        ticket = models.Ticket.objects.create(
            column=sample_column(),
            ticket_title='Test ticket title',
            ticket_description='Test ticket description',
            user=sample_user()
        )

        self.assertEqual(str(ticket), ticket.ticket_title)

    def test_create_label_str(self):
        """Test the project string representation"""
        label = models.Label.objects.create(
            label_name='Test label name',
            label_color='0xFFFFFF'
        )

        self.assertEqual(str(label), label.label_name)

    def test_create_comment_str(self):
        """Test the project string representation"""
        commented_by = get_user_model().objects.create(
            username='Test2',
            password='test123'
        )
        comment = models.Comment.objects.create(
            ticket=sample_ticket(),
            message='Test comment message',
            user=commented_by
        )

        self.assertEqual(str(comment), comment.message)
