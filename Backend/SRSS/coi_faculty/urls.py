# C:\Users\simmo\Downloads\Project-For-Software-Engineering-\backend\SRSS\coi_faculty\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.position_list, name='position_list'),
    path('post/', views.post_position, name='post_position'),
]