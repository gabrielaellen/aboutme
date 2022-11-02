from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class About(models.Model):
    first_name = models.CharField(max_length=10, default='')
    second_name = models.CharField(max_length=10,default='')
    description = models.TextField(default='')
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    link = models.URLField(max_length=200, default='')
    link_2 = models.URLField(max_length=200, default='')

    def __str__(self):
        return self.first_name

class Experience(models.Model):
    profession = models.CharField(max_length=30)
    company = models.CharField(max_length=60)
    description = models.TextField(blank=False)


    def __str__(self):
        return self.profession

class Education(models.Model):
    course = models.CharField(max_length=30)
    institution = models.CharField(max_length=60)
    

    def __str__(self):
        return self.course

class Skills(models.Model):
    workflow = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.workflow

