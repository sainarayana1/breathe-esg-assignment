from django.urls import path
from django.http import JsonResponse

def ingestion_home(request):
    return JsonResponse({
        "message": "Ingestion API Working"
    })

urlpatterns = [
    path('', ingestion_home),
]
