# employers/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.employer_profile_list, name='employer_profile_list'),  
    path('<int:user_id>/', views.employer_profile_detail, name='employer_profile_detail'),
    path('list/', views.employer_profile_list, name='employers'),  
]
