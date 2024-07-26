# employers/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.employer_profile_list, name='employer_profile_list'),  # Corrected view name
    path('<int:user_id>/', views.employer_profile_detail, name='employer_profile_detail'),
]
