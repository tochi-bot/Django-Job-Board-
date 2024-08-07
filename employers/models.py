
# employers/models.py

from django.db import models
from django.contrib.auth.models import User

# The EmployerProfile model extends the User model to store additional information specific to employers.
class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)  # Links to the User model, ensuring a one-to-one relationship.
    company_name = models.CharField(max_length=255, unique=True)  # Stores the name of the employer's company.
    website = models.URLField()  # Stores the URL of the employer's website.
    description = models.TextField()  # Stores a detailed description of the employer's company.

    def __str__(self):
        return self.company_name  # Returns the company name when the object is printed.

class Job(models.Model):
    employer = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant_name = models.CharField(max_length=255)
    applicant_email = models.EmailField()
    cover_letter = models.TextField()

    def __str__(self):
        return f"{self.applicant_name} for {self.job.title}"