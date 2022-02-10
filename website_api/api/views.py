from msilib.schema import ServiceInstall
from django.shortcuts import render
from rest_framework import generics
from api.serializers import UserSerializer
from .models import User
# from rest_framework import generics
# from .serializers import RoomSerializer
# from .models import Room

# Create your views here.


class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
