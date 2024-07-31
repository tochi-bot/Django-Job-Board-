
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import JobSeekerProfile, EmployerProfile, JobListing, Application
from .forms import JobListingForm, ApplicationForm
# View for the homepage
def index(request):
    return render(request, 'jobs/index.html')

# View for listing all job postings
def job_listings(request):
    jobs = JobListing.objects.all()
    return render(request, 'jobs/job_listings.html', {'jobs': jobs})

# View for job listing details
def job_listing_detail(request, job_id):
    job = get_object_or_404(JobListing, pk=job_id)
    return render(request, 'jobs/job_listing_detail.html', {'job': job})

# View for creating a job application
@login_required
def apply_for_job(request, job_id):
    job = get_object_or_404(JobListing, pk=job_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job_seeker = JobSeekerProfile.objects.get(user=request.user)
            application.job_listing = job
            application.save()
            return redirect('job_listing_detail', job_id=job.id)
    else:
        form = ApplicationForm()
    return render(request, 'jobs/apply_for_job.html', {'form': form, 'job': job})

# View for employer profile
def employer_profile(request, employer_id):
    employer = get_object_or_404(EmployerProfile, user__id=employer_id)
    job_listings = JobListing.objects.filter(employer=employer)
    return render(request, 'jobs/employer_profile.html', {'employer': employer, 'job_listings': job_listings})

# View for job seeker profile
@login_required
def job_seeker_profile(request):
    job_seeker = get_object_or_404(JobSeekerProfile, user=request.user)
    applications = Application.objects.filter(job_seeker=job_seeker)
    return render(request, 'jobs/job_seeker_profile.html', {'job_seeker': job_seeker, 'applications': applications})
