from django.urls import path
from . import views

urlpatterns = [
    path('resumes/', views.browse_resumes, name='browse_resumes'),
    path('student/<int:student_id>/', views.view_student_profile, name='view_student_profile'),
    path('search-opportunities/', views.search_research_opportunities, name='search_research_opportunities'),
]
