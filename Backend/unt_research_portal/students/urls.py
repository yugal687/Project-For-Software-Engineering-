from django.urls import path, include
from .views import StudentLoginView
from rest_framework.routers import DefaultRouter
from professor.views import ResearchOpportunityViewSet





router = DefaultRouter()
router.register('opportunity', ResearchOpportunityViewSet)

# router.register('', views.ProfessorView)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', StudentLoginView.as_view(), name='student-login'),
]
