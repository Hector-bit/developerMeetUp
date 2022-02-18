from django import forms
from .models import User, Project

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['host_name', 'project_title', 'project_description', 'project_contact']