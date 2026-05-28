from django.urls import path

from .views import (
    ReviewEmissionView,
    ESGDashboardView,
    TopEmissionSourcesView,
    ESGAnalyticsView,
    ESGSummaryReportView,
    ESGHealthScoreView,
    CompanyBenchmarkView,
    PDFReportView
)

urlpatterns = [

    path(
        "review/<int:record_id>/",
        ReviewEmissionView.as_view()
    ),

    path(
        "dashboard/",
        ESGDashboardView.as_view()
    ),

    path(
        "top-sources/",
        TopEmissionSourcesView.as_view()
    ),

    path(
        "analytics/",
        ESGAnalyticsView.as_view()
    ),

    path(
        "summary-report/",
        ESGSummaryReportView.as_view()
    ),

    path(
        "health-score/",
        ESGHealthScoreView.as_view()
    ),

    path(
        "benchmark/",
        CompanyBenchmarkView.as_view()
    ),

    path(
        "pdf-report/",
        PDFReportView.as_view()
    ),
]