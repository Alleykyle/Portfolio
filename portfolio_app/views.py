from django.shortcuts import render

def home(request):
    return render(request, "portfolio_app/home.html")

def dental_project(request):
    return render(request, "portfolio_app/projects/dental.html")

def dental_patients(request):
    return render(
        request,
        "portfolio_app/projects/dental_patients.html"
    )