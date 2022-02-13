from msilib.schema import ServiceInstall
from django.shortcuts import render
from rest_framework import generics
from api.serializers import CreateProjectSerializer, UserSerializer
from .models import User, Project
# from rest_framework import generics
# from .serializers import RoomSerializer
# from .models import Room

# Create your views here.


class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class ProjectView(generics.ListAPIView):
#     queryset = Projects.objects.all()
#     serializer_class = ProjectSerializer

# class CreateProject(generics.CreateAPIView):
#     serializer_project = CreateProjectSerializer

    # def post(self, request, format=None):
    #     if not 
