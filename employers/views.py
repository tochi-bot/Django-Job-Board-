# employers/views.py

from django.shortcuts import render, get_object_or_404
from .models import EmployerProfile

def employer_profile_list(request):
    """
    View to list all employer profiles.
    """
    # Retrieve all EmployerProfile objects from the database
    profiles = EmployerProfile.objects.all()
    # Render the 'employer_profile_list.html' template with the retrieved profiles
    return render(request, 'employers/employer_profile_list.html', {'profiles': profiles})

def employer_profile_detail(request, user_id):
    """
    View to show details of a specific employer profile.
    """
    # Retrieve a single EmployerProfile object based on the provided user_id or return a 404 error if not found
    profile = get_object_or_404(EmployerProfile, user_id=user_id)
    # Render the 'employer_profile_detail.html' template with the retrieved profile
    return render(request, 'employers/employer_profile_detail.html', {'profile': profile})


