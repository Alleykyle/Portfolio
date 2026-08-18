from django.shortcuts import render

def home(request):
    return render(request, "portfolio_app/home.html")


def dental_project(request):
    return render(
        request,
        "portfolio_app/projects/dental.html",
        {
            "active_page": "dashboard"
        }
    )


def dental_patients(request):
    return render(
        request,
        "portfolio_app/projects/dental_patients.html",
        {
            "active_page": "patients"
        }
    )

def dental_overview(request):
    return render(
        request,
        "portfolio_app/projects/dental_overview.html"
    )

def dental_appointments(request):
    return render(
        request,
        "portfolio_app/projects/dental_appointments.html",
        {
            "active_page": "appointments"
        }
    )

def dental_conversations(request):
    return render(
        request,
        "portfolio_app/projects/dental_conversations.html",
        {
            "active_page": "conversations"
        }
    )

def dental_reports(request):
    return render(
        request,
        "portfolio_app/projects/dental_reports.html",
        {"active_page": "reports"}
    )

def dental_settings(request):
    return render(
        request,
        "portfolio_app/projects/dental_settings.html",
        {"active_page": "settings"}
    )

def dental_workflows(request):
    return render(
        request,
        "portfolio_app/projects/dental_workflows.html",
        {"active_page": "workflows"}
    )

def dental_email(request):
    return render(
        request,
        "portfolio_app/projects/dental_email.html",
        {"active_page": "email"}
    )


def dental_dashboard(request):

    return render(

        request,

        "portfolio_app/projects/dental_dashboard.html",

        {

            "active_page":"dashboard"

        }

    )

def gym_dashboard(request):
    return render(request, "portfolio_app/projects/gym/dashboard.html")


def gym_members(request):
    return render(request, "portfolio_app/projects/gym/members.html")


def gym_trainers(request):
    return render(request, "portfolio_app/projects/gym/trainers.html")


def gym_memberships(request):
    return render(request, "portfolio_app/projects/gym/memberships.html")


def gym_schedule(request):
    return render(request, "portfolio_app/projects/gym/schedule.html")


def gym_payments(request):
    return render(request, "portfolio_app/projects/gym/payments.html")


def gym_reports(request):
    return render(request, "portfolio_app/projects/gym/reports.html")

def gym_attendance(request):
    return render(request, "portfolio_app/projects/gym/attendance.html")


def gym_settings(request):
    return render(request, "portfolio_app/projects/gym/settings.html")

def gym_overview(request):
    return render(
        request,
        "portfolio_app/projects/gym/overview.html"
    )