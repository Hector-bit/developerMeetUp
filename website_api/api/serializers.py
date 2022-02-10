from dataclasses import field
from rest_framework import serializers
from .models import User
from .models import Projects

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", 'username')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ("id", "project_name", "project_description", "project_host", "project_contact")
