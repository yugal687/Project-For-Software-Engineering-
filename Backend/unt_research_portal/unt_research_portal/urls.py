
from django.contrib import admin
from django.urls import path, include
from research import views
from professor.views import ProfessorView
from rest_framework import routers 
from django.conf import settings
from django.conf.urls.static import static

# router = routers.DefaultRouter

# # router.register(r'professor',  ProfessorView)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/professor/', include('professor.urls')),
    path('api/student/', include('students.urls')),
    path('api/coi-staff/', include('coi_staff.urls')),
    path('', include('research.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
