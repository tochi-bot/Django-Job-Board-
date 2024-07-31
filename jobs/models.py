# jobs/models.py

from django.db import models
from django.contrib.auth.models import User

# The EmployerProfile model extends the User model to store additional information specific to employers.
class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="jobs_employer_profile")  # Links to the User model, ensuring a one-to-one relationship.
    company_name = models.CharField(max_length=255, unique=True)  # Stores the name of the employer's company.
    website = models.URLField()  # Stores the URL of the employer's website.
    description = models.TextField()  # Stores a detailed description of the employer's company.

    def __str__(self):
        return self.company_name  # Returns the company name when the object is printed.


# The JobSeekerProfile model extends the User model to store additional information specific to job seekers.
class JobSeekerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="job_seeker_profile")  # Links to the User model, ensuring a one-to-one relationship.
    resume = models.FileField(upload_to='resumes/')  # Allows job seekers to upload their resume.
    skills = models.TextField() # Stores a list of the job seeker's skills.
    
    def __str__(self):
        return self.user.username 


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
