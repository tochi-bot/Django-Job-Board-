# Import modules from Django
from django import forms

# Import the Message model
from .models import Message

# Define the MessageForm class using ModelForm
class MessageForm(forms.ModelForm):
    # Meta class to specify the model and fields to be used in the form
    class Meta:
        model = Message  # Specify the model to use for the form
        fields = ['receiver', 'newjoblisting', 'content']  # Specify the fields to include in the form
