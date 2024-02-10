from django.contrib import admin
from base.models import *

# Register your models here.

class JobDescriptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'jobdescription']
    search_fields = ['user__username'] 

class ResumeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'resumes']
    search_fields = ['user__username'] 



admin.site.register(JobDescription, JobDescriptionAdmin)
admin.site.register(Resume,ResumeAdmin)