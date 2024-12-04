from django.urls import path
from .views import StudentLoginView, StudentResumeAnalysisView, StudentResumeUploadView

urlpatterns = [
    path('login/', StudentLoginView.as_view(), name='student-login'),
    path('<int:student_id>/analyze-resume/', StudentResumeAnalysisView.as_view(), name='student-resume-analysis'),
    path('<int:student_id>/upload-resume/', StudentResumeUploadView.as_view(), name='student-resume-upload'),
]
