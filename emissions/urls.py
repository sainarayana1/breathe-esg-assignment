from django.urls import path
from django.http import JsonResponse


def dashboard(request):
    return JsonResponse({
        "message": "Dashboard API Working"
    })


def analytics(request):
    return JsonResponse({
        "message": "Analytics API Working"
    })


def top_sources(request):
    return JsonResponse({
        "message": "Top Sources API Working"
    })


def summary_report(request):
    return JsonResponse({
        "message": "Summary Report API Working"
    })


def pdf_report(request):
    return JsonResponse({
        "message": "PDF Report API Working"
    })


urlpatterns = [
    path('dashboard/', dashboard),
    path('analytics/', analytics),
    path('top-sources/', top_sources),
    path('summary-report/', summary_report),
    path('pdf-report/', pdf_report),
]
