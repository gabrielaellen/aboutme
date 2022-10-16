from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class About(models.Model):
    name = models.CharField(max_length=30)
    avatar = models.URLField(blank=True, null=True)
    mini_about = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class Experience(models.Model):
    profession = models.CharField(max_length=30)
    company = models.CharField(max_length=60)
    description = models.TextField(blank=False)


    def __str__(self):
        return self.profession

class Education(models.Model):
    course = models.CharField(max_length=30)
    institution = models.CharField(max_length=40)
    

    def __str__(self):
        return self.course

class Skills(models.Model):
    skill = models.CharField(max_length=50, blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.skill

