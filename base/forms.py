from django import forms
from .models import JobDescription, Resume

class JobDescriptionForm(forms.ModelForm):
    class Meta:
        model = JobDescription
        fields = ['jobdescription', 'skills', 'education', 'age', 'experience']

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['resumes', 'count']
