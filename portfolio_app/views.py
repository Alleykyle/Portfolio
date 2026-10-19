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


def ghl_dental(request):
    screenshots = [
        {"image": "portfolio_app/images/form.png", "title": "1. Consultation Form",
         "desc": "Captures name, email, phone, and preferred contact time, with SMS consent."},
        {"image": "portfolio_app/images/1.png", "title": "2. Workflow: Trigger, Email, Team Alert",
         "desc": "On form submission, the lead gets a confirmation email and the team is notified."},
        {"image": "portfolio_app/images/2.png", "title": "3. Workflow: Tag, Pipeline, Wait",
         "desc": "The lead is tagged, added to the pipeline, then the workflow waits."},
        {"image": "portfolio_app/images/3.png", "title": "4. Workflow: Not Booked / Booked",
         "desc": "A condition checks for the booked tag, so only unbooked leads get the follow-up."},
        {"image": "portfolio_app/images/5.png", "title": "5. Test A: Not Booked",
         "desc": "Execution log showing the follow-up email sent."},
        {"image": "portfolio_app/images/4.png", "title": "6. Test B: Booked",
         "desc": "Execution log showing the workflow ending with no follow-up."},
        {"image": "portfolio_app/images/6.png", "title": "7. Pipeline Board",
         "desc": "Leads by stage: New Lead, Contacted, Booked, Completed."},
    ]
    loom_url = ""  # paste your Loom embed link here later
    return render(request, "portfolio_app/ghl_dental.html",
                  {"screenshots": screenshots, "loom_url": loom_url})