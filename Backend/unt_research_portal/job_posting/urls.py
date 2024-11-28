from django.urls import path
from .views import JobPostingListCreateView, JobPostingRetrieveUpdateDestroyView

urlpatterns = [
    path('job-postings/', JobPostingListCreateView.as_view(), name='job-postings-list-create'),
    path('job-postings/<int:pk>/', JobPostingRetrieveUpdateDestroyView.as_view(), name='job-posting-detail'),
]
