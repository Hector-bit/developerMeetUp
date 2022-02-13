from msilib.schema import ServiceInstall
from django.shortcuts import render
from rest_framework import generics
from api.serializers import CreateProjectSerializer, UserSerializer
from .models import User, Project

# Create your views here.
class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

