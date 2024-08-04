from django.contrib import admin
from .models import About, ContactRequest
from django_summernote.admin import SummernoteModelAdmin

# Register the About model with the admin site using the SummernoteModelAdmin.
# This allows the content field to use the Summernote WYSIWYG editor in the admin interface.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    # Specify which fields should use the Summernote editor.
    summernote_fields = ('content',)

# Register the ContactRequest model with the admin site using the SummernoteModelAdmin.
@admin.register(ContactRequest)
class ContactRequestAdmin(SummernoteModelAdmin):
    # Specify which fields should use the Summernote editor.
    summernote_fields = ('message',)
    # Define the fields to display in the list view of the admin interface.
    list_display = ('name', 'email', 'message', 'read')
