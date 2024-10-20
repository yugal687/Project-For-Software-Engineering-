
from django.urls import path
from . import views

urlpatterns = [
    # path('analyze/', views.analyze_text_view, name='analyze_text'),
    path('register/student/', views.register_student, name='register_student'),
    path('register/professor/', views.register_professor, name='register_professor'),
    path('register/coi_staff/', views.register_coi_staff, name='register_coi_staff'),
    path('register/super_admin/', views.register_super_admin, name='register_super_admin'),
    path('', views.home, name='home'),
]