from django.urls import path, include
from .views import COIStaffLoginView, COIStaffDashboardView, CSRFTokenView, ManageDocumentsView, StaffView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
#READ
#Create


router.register('', StaffView)  

urlpatterns = [
    path('login/', COIStaffLoginView.as_view(), name='coi-staff-login'),
    path('dashboard/', COIStaffDashboardView.as_view(), name='coi-staff-dashboard'),
    path('csrf/', CSRFTokenView.as_view(), name='csrf-token'),
    path('manage-documents/', ManageDocumentsView.as_view(), name='manage-documents'),
    path('', include(router.urls)),
    # path('documents/', CoiDocumentsView.as_view(), name='coi-documents'),
    # path('documents/<int:pk>/', CoiDocumentsView.as_view(), name='update-coi-document'),
    # path('consent-form/', ConsentFormView.as_view(), name='consent-form'),
    # path('nda/', NDAAcknowledgmentView.as_view(), name='nda-acknowledgment'),
]