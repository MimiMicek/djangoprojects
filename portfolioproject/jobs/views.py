from django.shortcuts import render
from .models import Job

def home(request):
    #passing the list of jobs to the view

    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})
