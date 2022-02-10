from operator import mod
from pyexpat import model
from statistics import mode
from django.db import models



# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=26, unique=True)

class Projects(model.Model):
    project_name = models.CharField(max_length=500)
    project_description = models.CharField()
    project_host = models.CharField()
    project_contact = models.CharField()
