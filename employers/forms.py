# employers/forms.py
# Importing the forms module from Django
from django import forms

# Importing the Application model from the current app's models module
from .models import Application

# Defining a form class for the Application model using ModelForm
class ApplicationForm(forms.ModelForm):
    # Meta class to specify which model and fields to include in the form
    class Meta:
        # The model that this form is based on
        model = Application
        # The fields of the Application model to include in the form
        fields = ['applicant_name', 'applicant_email', 'cover_letter']
