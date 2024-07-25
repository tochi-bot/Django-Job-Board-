from django.db import models
from django.contrib.auth.models import User

# The EmployerProfile model extends the User model to store additional information specific to employers.
class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Links to the User model, ensuring a one-to-one relationship.
    company_name = models.CharField(max_length=255)  # Stores the name of the employer's company.
    company_description = models.TextField()  # Stores a detailed description of the employer's company.

# The JobSeekerProfile model extends the User model to store additional information specific to job seekers.
class JobSeekerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Links to the User model, ensuring a one-to-one relationship.
    resume = models.FileField(upload_to='resumes/')  # Allows job seekers to upload their resume.
    skills = models.TextField()  # Stores a list of the job seeker's skills.

# The JobListing model represents a job post created by an employer.
class JobListing(models.Model):
    employer = models.ForeignKey(User, on_delete=models.CASCADE)  # Links to the User model, indicating the employer who posted the job.
    title = models.CharField(max_length=255)  # Stores the job title.
    description = models.TextField()  # Stores a detailed description of the job.
    location = models.CharField(max_length=255)  # Stores the job location.
    posted_at = models.DateTimeField(auto_now_add=True)  # Records the date and time when the job was posted.

# The Application model represents a job application submitted by a job seeker for a specific job listing.
class Application(models.Model):
    job_seeker = models.ForeignKey(User, on_delete=models.CASCADE)  # Links to the User model, indicating the job seeker who applied.
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE)  # Links to the JobListing model, indicating the job being applied for.
    applied_at = models.DateTimeField(auto_now_add=True)  # Records the date and time when the application was submitted.
    status = models.CharField(
        max_length=50,
        choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')]
    )  # Stores the status of the application, with predefined choices.
