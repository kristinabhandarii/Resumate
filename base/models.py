from django.db import models
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your models here.
User=get_user_model()
class HRmanager(models.Model):
    pass


class  JobDescription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    jobdescription = models.FileField(upload_to='jobdescription', null= True)
    skills = models.IntegerField(default=1)
    education = models.IntegerField(default=1)
    age = models.IntegerField(default=1)
    experience = models.IntegerField(default=1)
    
    def __str__(self):
        return f'JobDescription object ({self.user})'
    

class Resume(models.Model):
    shortlist=[(i, i) for i in range(1, 101)]
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    resumes = models.FileField(upload_to='resumes', null=True)
    count = models.IntegerField(default=1,choices=shortlist)

    def __str__(self):
        return f'Resume object ({self.user})'