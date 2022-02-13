from operator import mod, truediv
from pyexpat import model
from statistics import mode
from django.db import models



# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=26, unique=True)
    email = models.EmailField(max_length=100)
    passwd = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Project(models.Model):
    project_name = models.CharField(max_length=180)
    project_description = models.CharField(max_length=2500)
    project_host = models.CharField(max_length=40)
    project_contact = models.CharField(max_length=500)

    def __str__(self):
        return self.project_name + ' by ' + self.project_host
