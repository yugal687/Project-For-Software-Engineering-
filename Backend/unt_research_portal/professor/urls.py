from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfessorView, ResearchOpportunityViewSet
from django.contrib import admin
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)
from . import views
from .views import ProfessorLoginView, ProfessorDashboardView, CSRFTokenView, ApplyResearchOpportunityView, ManageApplicationsView, ApplicationView



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
router.register('opportunity', views.ResearchOpportunityViewSet, basename='professor-opportunity')  # Register opportunities

router.register('applications', views.ApplicationView, basename="student-applications")
router.register('', views.ProfessorView, basename='list-professor')  # Distinguish from 'login/'


urlpatterns = [
    
    path('login/', ProfessorLoginView.as_view(), name='professor-login'),
    path('dashboard/', ProfessorDashboardView.as_view(), name='professor-dashboard'),
    path('csrf/', CSRFTokenView.as_view(), name='csrf-token'),
    # path('opportunity/apply/', ApplyResearchOpportunityView.as_view(), name='apply-research-opportunity'),
    # path('applications/', ManageApplicationsView.as_view(), name='manage-applications'),
    # path('applications/<int:application_id>/', ManageApplicationsView.as_view(), name='update-application'),
    path('', include(router.urls)),
]


#Create

# router.register('professor/<int: professor_id>/opportunity/create', views.ResearchOpportunityViewSet)

# test
# router.register('api/professor/login/', views.ProfessorLoginView.as_view())




# urlpatterns = [
#     # API routes
#     path('', include(router.urls)),
#     path('login/', ProfessorLoginView.as_view(), name='professor-login'),
#     path('dashboard/', ProfessorDashboardAPIView.as_view(), name='professor-dashboard')
    

    # path('createlogin/', views.ProfessorLoginView.as_view(), name='professor-login'),

    # test
    # path('/', views.ProfessorView.as_view(), name='professor_view')
    # test
    # path('list-research-opportunities/', views.list_research_opportunities, name='list_research_opportunities'),
    # path('create-research-opportunity/', views.create_research_opportunity, name='create_research_opportunity'),
    # path('update-research-opportunity/<int:opportunity_id>/', views.update_research_opportunity, name='update_research_opportunity'),
    # path('delete-research-opportunity/<int:opportunity_id>/', views.delete_research_opportunity, name='delete_research_opportunity'),
    # test ends
    
    # # Non-API routes
    # path('professor/', views.professor_dashboard, name='professor_dashboard'),  # Non-API professor dashboard
    # path('professor/opportunity/create/', views.create_professor_profile, name='create_professor_profile'),  # Non-API profile creation
# ]

# urlpatterns = [
#     path('api/', include(router.urls)),
#     path('api/professor', views.ProfessorViewSet.as_view(), name='professor'),
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     # path('signup/', views.professor_signup, name='professor_signup'),
#     # path('dashboard/', views.professor_dashboard, name='professor_dashboard'),
#     # path('', views.professor_dashboard, name='professor_dashboard'),  # This will point to /professor
#     # path('create-profile/', views.create_professor_profile, name='create_professor_profile'),
#     # path('list-research-opportunities/', views.list_research_opportunities, name='list_research_opportunities'),
#     # path('create-research-opportunity/', views.create_research_opportunity, name='create_research_opportunity'),
#     # path('update-research-opportunity/<int:opportunity_id>/', views.update_research_opportunity, name='update_research_opportunity'),
#     # path('delete-research-opportunity/<int:opportunity_id>/', views.delete_research_opportunity, name='delete_research_opportunity'),
# ]
