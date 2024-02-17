from django.db import models
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create your models here.

User = get_user_model()

class HRmanagerID(models.Model):
    HR_id = models.CharField(max_length=100)
    def __str__(self):
        return self.HR_id
    
class Resume(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    file = models.FileField(upload_to='resumes')
    resume_text_content = models.FileField(blank=True)

    def __str__(self):
        return f"Resume for {self.user.username}"

class HRUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    HR_id = models.OneToOneField(HRmanagerID,on_delete=models.CASCADE)
    jobdescription = models.FileField(upload_to='jobdescription', null= True)
    skills = models.IntegerField(default= 1)
    education = models.IntegerField(default=1)
    age = models.IntegerField(default=1)
    experience = models.IntegerField(default=1)
    shortlist=[(i, i) for i in range(1, 101)]
    resumes = models.ManyToManyField(Resume)
    count = models.IntegerField(default=1,choices=shortlist)
    jd_text_content = models.FileField(blank=True) 

    def __str__(self) -> str:
        return str(self.user)
