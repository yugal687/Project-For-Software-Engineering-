
from django.contrib import admin
from django.urls import path, include
from research import views
# from professor.views import ProfessorView
from rest_framework import routers 


# router = routers.DefaultRouter

# # router.register(r'professor',  ProfessorView)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('research.urls')),
    path('api/professor/', include('professor.urls')),
    path('api/student/', include('students.urls')),
]


