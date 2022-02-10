from django.urls import path

from api.models import User
from .views import UserView

urlpatterns = [
    path('home', UserView.as_view()),
]