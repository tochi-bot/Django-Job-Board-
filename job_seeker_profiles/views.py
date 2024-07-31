# Import necessary modules from Django
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# Import the JobSeekerProfile model
from .models import JobSeekerProfile

# Import the JobSeekerProfileForm form
from .forms import JobSeekerProfileForm

# View for displaying the job seeker's profile
@login_required
def view_profile(request):
    # Get or create the JobSeekerProfile for the current user
    profile, created = JobSeekerProfile.objects.get_or_create(user=request.user)
    
    # Render the view_profile template with the profile context
    return render(request, 'job_seeker_profiles/view_profile.html', {'profile': profile})

# View for editing the job seeker's profile
@login_required
def edit_profile(request):
    # Get the JobSeekerProfile for the current user
    profile = get_object_or_404(JobSeekerProfile, user=request.user)
    
    if request.method == 'POST':
        # If the request method is POST, create a form instance with the POST data and files
        form = JobSeekerProfileForm(request.POST, request.FILES, instance=profile)
        
        if form.is_valid():
            # If the form is valid, save the form and redirect to the view_profile page
            form.save()
            return redirect('view_profile')
    else:
        # If the request method is not POST, create a form instance with the profile
        form = JobSeekerProfileForm(instance=profile)
    
    # Render the edit_profile template with the form context
    return render(request, 'job_seeker_profiles/edit_profile.html', {'form': form})
