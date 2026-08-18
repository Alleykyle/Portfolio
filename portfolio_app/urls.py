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
    path(
    "projects/dental-overview/",
    views.dental_overview,
    name="dental_overview",
    ),
    path(
    "projects/dental/appointments/",
    views.dental_appointments,
    name="dental_appointments",
    ),
    path(
    "projects/dental/conversations/",
    views.dental_conversations,
    name="dental_conversations",
    ),
    path(
    "projects/dental/reports/",
    views.dental_reports,
    name="dental_reports",
    ),
    path(
    "projects/dental/settings/",
    views.dental_settings,
    name="dental_settings",
    ),
    path(
    "projects/dental/workflows/",
    views.dental_workflows,
    name="dental_workflows",
    ),
    path(
    "projects/dental/email/",
    views.dental_email,
    name="dental_email",
    ),
    path(
    "projects/dental/dashboard/",
    views.dental_dashboard,
    name="dental_dashboard"
    ),
    path("projects/gym/", views.gym_dashboard, name="gym_dashboard"),
    path("projects/gym/members/", views.gym_members, name="gym_members"),
    path("projects/gym/trainers/", views.gym_trainers, name="gym_trainers"),
    path("projects/gym/memberships/", views.gym_memberships, name="gym_memberships"),
    path("projects/gym/schedule/", views.gym_schedule, name="gym_schedule"),
    path("projects/gym/payments/", views.gym_payments, name="gym_payments"),
    path("projects/gym/reports/", views.gym_reports, name="gym_reports"),
    path("projects/gym/attendance/", views.gym_attendance, name="gym_attendance"),
    path("projects/gym/settings/", views.gym_settings, name="gym_settings"),
    path(
        "projects/gym/overview/",
        views.gym_overview,
        name="gym_overview"
    ),
]