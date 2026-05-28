from django.http import JsonResponse


def home(request):
    return JsonResponse({
        "status": "success",
        "project": "Breathe ESG Internship Assignment",
        "message": "ESG Analytics Platform API is Live 🚀",

        "available_endpoints": {
            "admin": "/admin/",
            "dashboard": "/api/emissions/dashboard/",
            "analytics": "/api/emissions/analytics/",
            "top_sources": "/api/emissions/top-sources/",
            "summary_report": "/api/emissions/summary-report/",
            "pdf_report": "/api/emissions/pdf-report/",
            "companies": "/api/companies/",
            "audits": "/api/audits/",
            "ingestion": "/api/ingestion/"
        }
    })