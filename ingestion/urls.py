from django.urls import path
from django.http import JsonResponse


def ingestion_home(request):
    return JsonResponse({
        "status": "success",
        "message": "Data Ingestion API Working"
    })


urlpatterns = [
    path('', ingestion_home),
]
