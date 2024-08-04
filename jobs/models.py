# jobs/models.py

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class JobSeekerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='job_seeker_profile_from_jobs')
    profile_image = CloudinaryField('image', blank=True, null=True)
    resume = models.FileField(upload_to='resumes/',blank=True, null=True)
    skills = models.TextField()

    def __str__(self):
        return self.user.username

class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employer_profile')
    company_name = models.CharField(max_length=255, unique=True)
    website = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.company_name

# The JobListing model represents a job post created by an employer.
class JobListing(models.Model):
    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="job_listings")  # Links to the User model, indicating the employer who posted the job.
    title = models.CharField(max_length=255)  # Stores the job title.
    description = models.TextField()  # Stores a detailed description of the job.
    location = models.CharField(max_length=255)  # Stores the job location.
    posted_at = models.DateTimeField(auto_now_add=True)  # Records the date and time when the job was posted.

    def __str__(self):
        return self.title  # Returns the job title when the object is printed.


# The Application model represents a job application submitted by a job seeker for a specific job listing.
class Application(models.Model):
    job_seeker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")  # Links to the User model, indicating the job seeker who applied.
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE, related_name="applications")  # Links to the JobListing model, indicating the job being applied for.
    applied_at = models.DateTimeField(auto_now_add=True)  # Records the date and time when the application was submitted.
    status = models.CharField(
        max_length=50,
        choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')]  # Provides predefined choices for the application status.
    )

    def __str__(self):
        return f"{self.job_seeker} applied for {self.job_listing}"  # Returns a string representation of the application.


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="jobs_sent_messages")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="jobs_received_messages")
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE, related_name="jobs_messages")
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
