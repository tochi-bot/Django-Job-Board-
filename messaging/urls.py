# Import necessary modules from Django
from django.urls import path

# Import the views from the current app
from . import views

# Define the URL patterns for the app
urlpatterns = [
    # URL pattern for the send_message view
    path('send/', views.send_message, name='send_message'),
    
]
