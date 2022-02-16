from pyexpat import model
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Project(models.Model):
    host_name = models.CharField(max_length=50)
    project_title = models.CharField(max_length=120)
    project_description = models.CharField(max_length=2000)
    project_contact = models.CharField(max_length=1000)

    def __str__(self):
        return "USERNAME: " + self.host_name + " PROJECT: " + self.project_title

