from django.urls import path
from . import views  # Import views from the current module

urlpatterns = [
    path('', views.about, name='about'),]