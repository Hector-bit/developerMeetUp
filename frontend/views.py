from curses import ALL_MOUSE_EVENTS
from django.shortcuts import render
from .models import User, Project

# Create your views here.
def home(request):
    all_projects = Project.objects.all
    return render(request, "home.html", {'all': all_projects})

def join(request):
    return render (request, 'join.html', {})