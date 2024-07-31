# Import necessary modules from Django
from django.urls import path

# Import the views from the current app
from .views import view_profile, edit_profile

# Define the URL patterns for the app
urlpatterns = [
    # URL pattern for viewing the job seeker's profile
    path('profile/', view_profile, name='view_profile'),
    
    # URL pattern for editing the job seeker's profile
    path('profile/edit/', edit_profile, name='edit_profile'),
]
