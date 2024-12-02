from django.urls import path, include
from rest_framework.routers import DefaultRouter
from professor.views import ResearchOpportunityViewSet
from .views import StudentLoginView, StudentDashboardView, StudentLogoutView, CSRFTokenView, get_csrf_token




router = DefaultRouter()
# router.register('opportunity', ResearchOpportunityViewSet)

# router.register('', views.ProfessorView)

urlpatterns = [
    # path('', include(router.urls)),
    path('login/', StudentLoginView.as_view(), name='student-login'),
    path('dashboard/', StudentDashboardView.as_view(), name='student-dashboard'),
    path('logout/', StudentLogoutView.as_view(), name='student-logout'),
    # path('csrf/', CSRFTokenView.as_view(), name='csrf-token'),
    path('csrf/', get_csrf_token, name='get_csrf_token'),
]
