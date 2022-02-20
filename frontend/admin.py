from django.contrib import admin
from .models import User, Project

#this is where you register your models
admin.site.register(User)
admin.site.register(Project)



