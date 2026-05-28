from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', dashboard),
    path('analytics/', analytics),
    path('top-sources/', top_sources),
    path('summary-report/', summary_report),
    path('pdf-report/', pdf_report),
]
