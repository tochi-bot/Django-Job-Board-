from django.contrib import admin
from .models import JobSeekerProfile, EmployerProfile, JobListing, Application, Notification, Message
from .forms import JobSeekerProfileForm

class JobSeekerProfileAdmin(admin.ModelAdmin):
    form = JobSeekerProfileForm
    list_display = ('user',)
    search_fields = ('user__username',)
    fields = ('user', 'profile_image', 'resume')

# Register the model with the admin class only once
try:
    admin.site.unregister(JobSeekerProfile)  # Unregister if already registered
except admin.sites.NotRegistered:
    pass

admin.site.register(JobSeekerProfile, JobSeekerProfileAdmin)

# Register other models
admin.site.register(EmployerProfile)
admin.site.register(JobListing)
admin.site.register(Application)
admin.site.register(Notification)
admin.site.register(Message)


