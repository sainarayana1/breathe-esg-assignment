from django.urls import path
from django.http import JsonResponse


def audits_home(request):
    return JsonResponse({
        "status": "success",
        "message": "Audits API Working"
    })


urlpatterns = [
    path('', audits_home),
]
