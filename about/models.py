from django.db import models

# Model to store information about the "About" section
class About(models.Model):
    # Title of the about section
    title = models.CharField(max_length=200)
    # Timestamp that updates automatically whenever the record is updated
    updated_on = models.DateTimeField(auto_now=True)
    # Content of the about section
    content = models.TextField()

    def __str__(self):
        # String representation of the model, showing the title
        return self.title

# Model to store collaboration requests from users
class ContactRequest(models.Model):
    # Name of the person requesting collaboration
    name = models.CharField(max_length=200)
    # Email address of the person requesting collaboration
    email = models.EmailField()
    # Message content of the collaboration request
    message = models.TextField()
    # Boolean flag to mark the request as read or unread
    read = models.BooleanField(default=False)

    def __str__(self):
        # String representation of the model, showing the name of the requester
        return f"Collaboration request from {self.name}"
