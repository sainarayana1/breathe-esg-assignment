from django.urls import path
from django.http import JsonResponse

def audits_home(request):
    return JsonResponse({
        "message": "Audits API Working"
    })

urlpatterns = [
    path('', audits_home),
]
