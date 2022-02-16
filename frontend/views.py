from django.shortcuts import render
from .models import User, Project

# Create your views here.
def home(request):
    all_users = User.objects.all
    return render(request, "home.html", {'all': all_users})

