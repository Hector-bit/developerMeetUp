from curses import ALL_MOUSE_EVENTS
from django.shortcuts import redirect, render
from django.shortcuts import render, redirect
from .models import User, Project
from .forms import UserForm, ProjectForm
from django.contrib import messages

# Create your views here.
def home(request):
    all_projects = Project.objects.all
    return render(request, "home.html", {'all': all_projects})

def post(request):
    if request.method == "POST":
        form = ProjectForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            host_name = request.POST['host_name']
            project_title = request.POST['project_title']
            project_description = request.POST['project_description']
            project_contact = request.POST['project_contact']

            messages.success(request, ('There are some missing requirments for your form'))
            return render(request, 'post.html', {'host_name': host_name, 'project_title':project_title,'project_description':project_description,'project_contact':project_contact})
        messages.success(request, ("Your post has beeen made"))
        return redirect("/")
    else:
        return render(request, 'post.html')
    
def join(request):
    if request.method == "POST":
        form = UserForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            username = request.POST['username']
            email = request.POST['email']
            
            messages.success(request, ('There was an error with your form'))

            return render(request, 'join.html', {'username':username, 'email':email})            
        messages.success(request, ("Your form has been submitted successfully"))
        return redirect("/")
    else:
        return render(request, 'join.html', {})