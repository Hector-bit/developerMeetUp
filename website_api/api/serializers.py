from dataclasses import field
from rest_framework import serializers
from .models import User, Project
# from .models import Projects

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", 'username')

class CreateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "project_name", "project_description", "project_host", "project_contact")
