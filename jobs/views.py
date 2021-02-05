from django.shortcuts import render, get_object_or_404
from .models import Job

def home(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/home.html', {
        'jobs': jobs
    })

def details(request, job_id):
    id = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/details.html', {
        'job': id
    })