# employers/views.py
from django.shortcuts import render, get_object_or_404
from .models import EmployerProfile, Job
from .forms import ApplicationForm

def employer_list(request):
    employers = EmployerProfile.objects.all()
    return render(request, 'employers/employer_list.html', {'employers': employers})

def employer_detail(request, employer_id):
    employer = get_object_or_404(EmployerProfile, pk=employer_id)
    jobs = employer.job_set.all()
    return render(request, 'employers/employer_detail.html', {'employer': employer, 'jobs': jobs})

def job_detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            return render(request, 'employers/application_success.html')
    else:
        form = ApplicationForm()
    return render(request, 'employers/job_detail.html', {'job': job, 'form': form})
