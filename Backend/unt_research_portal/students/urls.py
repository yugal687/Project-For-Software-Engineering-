from django.urls import path, include
from rest_framework.routers import DefaultRouter
from professor.views import ResearchOpportunityViewSet
from .views import StudentLoginView, StudentDashboardView, StudentLogoutView, StudentView, AllResearchOpportunitiesView, ApplyResearchOpportunityView, StudentApplicationView




router = DefaultRouter()
# router.register('opportunity', ResearchOpportunityViewSet)

router.register('', StudentView)
router.register('opportunity/apply', StudentApplicationView)

# router.register('get-active-opportunities', AllResearchOpportunitiesView)


urlpatterns = [
    
    path('login/', StudentLoginView.as_view(), name='student-login'),
    path('dashboard/', StudentDashboardView.as_view(), name='student-dashboard'),
    path('get-active-opportunities/', AllResearchOpportunitiesView.as_view(), name='active-opportunities'),
    path('application/getscore/', ApplyResearchOpportunityView.as_view(), name='student-score'),
    path('logout/', StudentLogoutView.as_view(), name='student-logout'),
    

    # path('opportunity/apply/', StudentApplicationView.as_view(), name='apply-research-opportunity'),
    path('', include(router.urls)),
    # path('csrf/', CSRFTokenView.as_view(), name='csrf-token'),
    # path('csrf/', get_csrf_token, name='get_csrf_token'),
]
