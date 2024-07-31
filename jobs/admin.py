from django.contrib import admin

from .models import JobSeekerProfile,EmployerProfile,JobListing, Application

# Register your models here.
admin.site.register(JobSeekerProfile)
admin.site.register(EmployerProfile)
admin.site.register(JobListing)
admin.site.register(Application)
