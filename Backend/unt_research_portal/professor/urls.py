from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfessorView, ResearchOpportunityViewSet, ProfessorLoginView, ProfessorDashboardAPIView
from django.contrib import admin
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)
from . import views

# router = DefaultRouter()
# router.register(r'professors', ProfessorViewSet, "professor")
# router.register(r'researchopportunities', ResearchOpportunityViewSet)

# urlpatterns = router.urls


router = DefaultRouter()
#READ
#Create


router.register('opportunity', views.ResearchOpportunityViewSet)
router.register('applications', views.ApplicationView)
router.register('', views.ProfessorView)


# router.register('opportunity/apply', StudentApplicationView)

# router.register('professor/<int: professor_id>/opportunity/create', views.ResearchOpportunityViewSet)

# test
# router.register('api/professor/login/', views.ProfessorLoginView.as_view())


urlpatterns = [
    # API routes

    path('login/', views.ProfessorLoginView.as_view(), name='professor-login'),
    # path('dashboard/', views.ProfessorProfileView.as_view(), name='detail'),
    path('dashboard/', views.get_professor_profile, name='detail'),

    # path('<pk>/', views.ProfessorView.as_view(), name="professor-detail"),
    path('', include(router.urls)),

    # path('csrf/', views.csrf, name='csrf'),
    
    
    
    
]

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



# 
# /professor/login(login-fetch)
# email : 
# password: 

# response: Token -> Localstorage or session storage
# front-> /dashboard


# dashboard (fetch)
# /professor/dashboard-detail
# [is_authenticated]
# response: Professor details