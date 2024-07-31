# Import necessary modules from Django
from django import forms

# Import the JobSeekerProfile model
from .models import JobSeekerProfile

# Define the JobSeekerProfileForm class using ModelForm
class JobSeekerProfileForm(forms.ModelForm):
    # Meta class to specify the model and fields to be used in the form
    class Meta:
        model = JobSeekerProfile  # Specify the model to use for the form
        fields = ['resume', 'skills']  # Specify the fields to include in the form
