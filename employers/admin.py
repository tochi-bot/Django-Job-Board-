from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import EmployerProfile

# Register your models here.
admin.site.register(EmployerProfile)