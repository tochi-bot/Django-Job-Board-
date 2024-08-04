from django.urls import path
from . import views  # Import views from the current module

urlpatterns = [
    path('', views.index, name='index'),
    path('jobs/<int:job_id>/', views.job_listing_detail, name='job_listing_detail'),
    path('jobs/', views.job_listings, name='job_list'),  
    path('jobs/<int:job_id>/apply/', views.apply_for_job, name='apply_for_job'),
    path('employer/<int:employer_id>/', views.employer_profile, name='employer_profile'),
    path('profile/', views.job_seeker_profile, name='job_seeker_profile'),
]
