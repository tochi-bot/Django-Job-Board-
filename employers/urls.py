# employers/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.employer_list, name='employer_list'),
    path('employer/<int:employer_id>/', views.employer_detail, name='employer_detail'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
]
