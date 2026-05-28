from django.urls import path
from django.http import JsonResponse


def dashboard(request):
    return JsonResponse({
        "status": "success",
        "endpoint": "dashboard",
        "message": "Emission Dashboard API Working"
    })


def analytics(request):
    return JsonResponse({
        "status": "success",
        "endpoint": "analytics",
        "message": "Emission Analytics API Working"
    })


def top_sources(request):
    return JsonResponse({
        "status": "success",
        "endpoint": "top-sources",
        "message": "Top Emission Sources API Working"
    })


def summary_report(request):
    return JsonResponse({
        "status": "success",
        "endpoint": "summary-report",
        "message": "Summary Report API Working"
    })


def pdf_report(request):
    return JsonResponse({
        "status": "success",
        "endpoint": "pdf-report",
        "message": "PDF Report API Working"
    })


urlpatterns = [
    path('dashboard/', dashboard),
    path('analytics/', analytics),
    path('top-sources/', top_sources),
    path('summary-report/', summary_report),
    path('pdf-report/', pdf_report),
]
