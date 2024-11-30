# For session authentication
from django.urls import path
from .views import StudentLoginView, StudentDashboardView, StudentLogoutView, CSRFTokenView

urlpatterns = [
    path('login/', StudentLoginView.as_view(), name='student-login'),
    path('dashboard/', StudentDashboardView.as_view(), name='student-dashboard'),
    path('logout/', StudentLogoutView.as_view(), name='student-logout'),
    path('csrf/', CSRFTokenView.as_view(), name='csrf-token'),
    
]


#For JWT Authentication
# from django.urls import path
# from .views import StudentRegistrationView, StudentLoginView, StudentDashboardView

# urlpatterns = [
#     path('register/', StudentRegistrationView.as_view(), name='student-register'),
#     path('login/', StudentLoginView.as_view(), name='student-login'),
#     path('dashboard/', StudentDashboardView.as_view(), name='student-dashboard'),
# ]
