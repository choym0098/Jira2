from rest_framework import serializers

from jira2app.models import UserProfile, Project, Column
from django.contrib.auth import get_user_model


class UserSerializer(serializers.Serializer):
    """Serializer for user objects"""
    
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')


class ColumnSerializer(serializers.Serializer):
    """Serializer for column objects"""

    class Meta:
        model = Column
        fields = ('id', 'column_name', 'next_column')


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for project objects"""
    users = UserSerializer(many=True)
    columns = ColumnSerializer(many=True)

    class Meta:
        model = Project
        fields = ('id', 'project_name', 'project_description', 'is_private',
                  'created_at', 'updated_at','users', 'columns')
