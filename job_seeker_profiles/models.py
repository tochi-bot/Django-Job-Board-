# Import necessary modules from Django
from django.db import models
from django.contrib.auth.models import User

# The JobSeekerProfile model extends the User model to store additional information specific to job seekers.
class JobSeekerProfile(models.Model):
    # Links to the User model, ensuring a one-to-one relationship.
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='job_seeker_profile_from_profiles')
    
    # Allows job seekers to upload their resume.
    resume = models.FileField(upload_to='resumes/')
    
    # Stores a list of the job seeker's skills.
    skills = models.TextField()

    # Returns the username of the job seeker when the object is printed.
    def __str__(self):
        return self.user.username
