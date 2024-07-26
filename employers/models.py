
# employers/models.py

from django.db import models
from django.contrib.auth.models import User

# EmployerProfile model to store additional information about employers
class EmployerProfile(models.Model):
    # One-to-one relationship with the User model; if the user is deleted, also delete the profile
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employer_profile_employers')
    # Field to store the name of the company, maximum length of 255 characters
    company_name = models.CharField(max_length=255)
    # Field to store a detailed description of the company
    company_description = models.TextField()
    
    # String representation of the model (useful for admin interface and debugging)
    def __str__(self):
        return self.company_name

