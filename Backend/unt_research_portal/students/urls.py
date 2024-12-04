# For session authentication
from django.urls import path, include
from .views import StudentLoginView, StudentDashboardView, StudentLogoutView, ApplyResearchOpportunityView, CSRFTokenView
from . import views
from rest_framework.routers import DefaultRouter




# router = DefaultRouter()
# router.register(r'professors', ProfessorViewSet, "professor")
# router.register(r'researchopportunities', ResearchOpportunityViewSet)

# urlpatterns = router.urls


# router = DefaultRouter()
# #Create
# router.register('opportunity', views.ResearchOpportunityViewSet)
# #READ
# router.register('', views.ProfessorView)

# Using Session 
router = DefaultRouter()
router.register('opportunity/apply', views.StudentApplicationView)  # Register opportunities


urlpatterns = [
    path('login/', StudentLoginView.as_view(), name='student-login'),
    path('dashboard/', StudentDashboardView.as_view(), name='student-dashboard'),
    path('logout/', StudentLogoutView.as_view(), name='student-logout'),
    # path('', include(router.urls)),
    
    path('resume/score/', ApplyResearchOpportunityView.as_view(), name='apply-research-opportunity'),
    path('csrf/', CSRFTokenView.as_view(), name='csrf-token'),
    path('', include(router.urls)),
    
]


#For JWT Authentication
# from django.urls import path
# from .views import StudentRegistrationView, StudentLoginView, StudentDashboardView

# urlpatterns = [
#     path('register/', StudentRegistrationView.as_view(), name='student-register'),
#     path('login/', StudentLoginView.as_view(), name='student-login'),
#     path('dashboard/', StudentDashboardView.as_view(), name='student-dashboard'),
# ]
