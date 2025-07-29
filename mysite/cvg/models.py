from django.db import models

# Create your models here.

class CvProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    summary = models.TextField()
    skills = models.TextField()
    experience = models.TextField()
    education = models.TextField()
    projects = models.TextField()
    interests = models.TextField()
    personal_info = models.TextField()
    work_experience = models.TextField()
    previous_employment = models.TextField()
    certifications = models.TextField()
    references = models.TextField()
    contact_info = models.TextField()
    other_skills = models.TextField()
