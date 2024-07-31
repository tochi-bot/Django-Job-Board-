# Import necessary modules from Django
from django.db import models
from django.contrib.auth.models import User

# Import the JobListing model from the jobs app
from jobs.models import JobListing  

# Define the Message model
class Message(models.Model):
    # The user who sends the message
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    
    # The user who receives the message
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    
    # The job listing associated with the message
    newjoblisting = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    
    # The content of the message
    content = models.TextField()
    
    # The timestamp when the message is sent
    sent_at = models.DateTimeField(auto_now_add=True)
