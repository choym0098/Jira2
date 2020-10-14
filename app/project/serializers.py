# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from jira2app.models import Column, Project, Ticket
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user objects"""

    class Meta:
        model = get_user_model()
        fields = ("id", "username")


class TicketSerializer(serializers.ModelSerializer):
    """Serializer for ticket objects"""
    user = UserSerializer(many=False)
    notifyees = UserSerializer(many=True)

    class Meta:
        model = Ticket
        fields = ("id", "created_at", "updated_at", "ticket_title", "ticket_description",
                  "user", "notifyees")


class ColumnSerializer(serializers.ModelSerializer):
    """Serializer for column objects"""
    tickets = TicketSerializer(many=True)

    class Meta:
        model = Column
        fields = ("id", "column_name", "next_column", "tickets")


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for project objects"""

    users = UserSerializer(many=True)
    columns = ColumnSerializer(many=True)

    class Meta:
        model = Project
        fields = (
            "id",
            "project_name",
            "project_description",
            "is_private",
            "created_at",
            "updated_at",
            "users",
            "columns",
        )
