from django.contrib import admin 
from django import forms
from .models import JobSeekerProfile
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


class JobSeekerProfileForm(forms.ModelForm):
    class Meta:
        model = JobSeekerProfile
        fields = ['user', 'profile_image', 'resume']
        widgets = {
            'profile_image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
            'resume': forms.ClearableFileInput(attrs={'accept': '.pdf,.doc,.docx'}),
        }





class JobSeekerProfileAdmin(admin.ModelAdmin):
    form = JobSeekerProfileForm
    list_display = ('user',)
    search_fields = ('user__username',)
    fields = ('user', 'profile_image', 'resume')

admin.site.register(JobSeekerProfile, JobSeekerProfileAdmin)
