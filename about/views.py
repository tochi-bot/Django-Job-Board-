from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import ContactRequestForm  # Correct import of the form

def about(request):
    # Retrieve the most recently updated 'About' instance
    about = About.objects.all().order_by('-updated_on').first()

    # Check if the request method is POST
    if request.method == 'POST':
        # Instantiate the form with POST data
        contact_form = ContactRequestForm(data=request.POST)
        
        # Validate the form
        if contact_form.is_valid():
            # Save the form data to the database
            contact_form.save()
            # Add a success message to be displayed to the user
            messages.add_message(request, messages.SUCCESS, "Contact request received! I endeavor to respond within 2 working days.")
    else:
        # Instantiate an empty form if the request method is GET
        contact_form = ContactRequestForm()

    # Render the 'about' template with the 'about' instance and the form
    return render(
        request,
        "about/about.html",
        {
            "about": about,  # Pass the 'about' instance to the template
            "contact_form": contact_form  # Pass the form to the template
        },
    )
