from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/dental/', views.dental_project, name='dental_project'),
    path(
    'projects/dental/patients/',
    views.dental_patients,
    name='dental_patients'
    ),
]