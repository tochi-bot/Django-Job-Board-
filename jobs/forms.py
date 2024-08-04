from django import forms
from .models import JobListing, Message, Application
 
class JobListingForm(forms.ModelForm):
    class Meta:
        model = JobListing
        fields = ['title', 'description', 'location']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['status']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
