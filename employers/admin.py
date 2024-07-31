from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import EmployerProfile


admin.site.register(EmployerProfile)
