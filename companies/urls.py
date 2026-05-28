from django.urls import path
from django.http import JsonResponse


def companies_home(request):
    return JsonResponse({
        "status": "success",
        "message": "Companies API Working"
    })


urlpatterns = [
    path('', companies_home),
]
