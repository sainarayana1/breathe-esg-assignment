"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse


# Home API
def home(request):
    return JsonResponse({
        "status": "success",
        "message": "ESG Analytics Platform API is Live 🚀",
        "available_endpoints": {
            "admin": "/admin/",
            "dashboard": "/api/emissions/dashboard/",
            "analytics": "/api/emissions/analytics/",
            "top_sources": "/api/emissions/top-sources/",
            "summary_report": "/api/emissions/summary-report/",
            "pdf_report": "/api/emissions/pdf-report/",
        }
    })


urlpatterns = [
    path('', home),

    path('admin/', admin.site.urls),

    path(
        'api/emissions/',
        include('emissions.urls')
    ),

    path(
        'api/audits/',
        include('audits.urls')
    ),

    path(
        'api/companies/',
        include('companies.urls')
    ),

    path(
        'api/ingestion/',
        include('ingestion.urls')
    ),
]
