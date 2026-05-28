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
from django.http import HttpResponse


# Home Page
def home(request):
    return HttpResponse(
        """
        <h1>ESG Analytics Platform is Live 🚀</h1>
        <p>Django REST API deployment successful.</p>

        <h3>Available APIs:</h3>

        <ul>
            <li>/admin/</li>
            <li>/api/emissions/dashboard/</li>
            <li>/api/emissions/analytics/</li>
            <li>/api/emissions/top-sources/</li>
            <li>/api/emissions/summary-report/</li>
            <li>/api/emissions/pdf-report/</li>
        </ul>
        """
    )


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
]
