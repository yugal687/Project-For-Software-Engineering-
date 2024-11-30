from django.urls import path
from .views import COIStaffLoginView, COIStaffDashboardView, CSRFTokenView

urlpatterns = [
    path('login/', COIStaffLoginView.as_view(), name='coi-staff-login'),
    path('dashboard/', COIStaffDashboardView.as_view(), name='coi-staff-dashboard'),
    path('csrf/', CSRFTokenView.as_view(), name='csrf-token'),
]