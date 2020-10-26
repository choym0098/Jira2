# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from jira2app.models import Column, Project, Ticket, Comment, Label
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user objects"""

    class Meta:
        model = get_user_model()
        fields = ("id", "username")


class LabelSerializer(serializers.ModelSerializer):
    """Serializer for label objects"""

    class Meta:
        model = Label
        fields = ("id", "label_name", "label_color")


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for comment objects"""
    user = UserSerializer(many=False)
    labels = LabelSerializer(many=True)

    class Meta:
        model = Comment
        fields = ("id", "created_at", "updated_at", "message", "user", "labels")


class TicketDetailSerializer(serializers.ModelSerializer):
    """Serializer detail ticket info to show when clicking tickets"""
    user = UserSerializer(many=False)
    notifyees = UserSerializer(many=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Ticket
        fields = ("id", "created_at", "updated_at", "ticket_title", "ticket_description",
                  "user", "notifyees", "comments")


class TicketSerializer(serializers.ModelSerializer):
    """Serialize simplified ticket info that are being used in project page"""

    class Meta:
        model = Ticket
        fields = ("id", "created_at", "updated_at", "ticket_title", "ticket_description",)


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
