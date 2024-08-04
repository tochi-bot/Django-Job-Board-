from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import JobSeekerProfile, EmployerProfile, JobListing, Message, Application
from .forms import JobListingForm, ApplicationForm
from django.contrib.auth.models import User
from .forms import MessageForm
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

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
    user = request.user  # Get the User instance
    job_seeker, created = JobSeekerProfile.objects.get_or_create(user=user)
    applications = Application.objects.filter(job_seeker=job_seeker)
    return render(request, 'jobs/job_seeker_profile.html', {'job_seeker': job_seeker, 'applications': applications})

@login_required
def chat(request, job_listing_id, receiver_id):
    job_listing = get_object_or_404(JobListing, id=job_listing_id)
    receiver = get_object_or_404(User, id=receiver_id)
    messages = Message.objects.filter(job_listing=job_listing, sender=request.user, receiver=receiver) | \
               Message.objects.filter(job_listing=job_listing, sender=receiver, receiver=request.user)
    messages = messages.order_by('sent_at')

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = receiver
            message.job_listing = job_listing
            message.save()
            return redirect('chat', job_listing_id=job_listing.id, receiver_id=receiver.id)
    else:
        form = MessageForm()

    return render(request, 'jobs/chat.html', {'job_listing': job_listing, 'receiver': receiver, 'messages': messages, 'form': form})

@receiver(post_save, sender=Application)
def send_application_notification(sender, instance, created, **kwargs):
    if created:
        job_listing = instance.job_listing
        employer = job_listing.employer
        subject = 'New Job Application'
        message = f'You have a new application for your job listing: {job_listing.title}.'
        email_from = 'noreply@jobboard.com'
        recipient_list = [employer.email]
        send_mail(subject, message, email_from, recipient_list)

        Notification.objects.create(
            user=employer,
            message=f'You have a new application for your job listing: {job_listing.title}.'
        )
