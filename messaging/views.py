# Import necessary modules from Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Import the Message model and MessageForm
from .models import Message
from .forms import MessageForm

# Define a view to handle sending messages
@login_required  # Ensure the user is logged in to access this view
def send_message(request):
    if request.method == 'POST':  # Check if the request method is POST
        form = MessageForm(request.POST)  # Create a form instance with the POST data
        if form.is_valid():  # Validate the form data
            message = form.save(commit=False)  # Create a message object without saving to the database yet
            message.sender = request.user  # Set the sender to the current logged-in user
            message.save()  # Save the message to the database
            return redirect('some-view-name')  # Redirect to an appropriate view after saving
    else:
        form = MessageForm()  # If the request method is not POST, create an empty form instance
    return render(request, 'messaging/send_message.html', {'form': form})  # Render the form in the template


