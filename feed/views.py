from multiprocessing import context
from django.shortcuts import render
from .models import About, Experience, Education, Skills

# Create your views here.
def index(request):

    about = About.objects.all()
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    skills = Skills.objects.all()

    context = {
        'about' : about,
        'experiences' : experiences,
        'educations' : educations,
        'skills' : skills
    }


    return render(request, 'index.html', context)