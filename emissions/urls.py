from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard),
    path("analytics/", views.analytics),
    path("top-sources/", views.top_sources),
    path("summary-report/", views.summary_report),
    path("pdf-report/", views.pdf_report),
]
