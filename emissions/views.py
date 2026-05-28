from django.http import JsonResponse


def dashboard(request):
    data = {
        "status": "success",
        "total_emissions": "2450 kg CO2",
        "companies_monitored": 12,
        "high_risk_companies": 3,
        "monthly_growth": "12%",
    }

    return JsonResponse(data)


def analytics(request):
    data = {
        "status": "success",
        "electricity": "40%",
        "travel": "35%",
        "fuel": "25%",
    }

    return JsonResponse(data)


def top_sources(request):
    data = {
        "status": "success",
        "top_sources": [
            "Electricity",
            "Travel",
            "Fuel"
        ]
    }

    return JsonResponse(data)


def summary_report(request):
    data = {
        "status": "success",
        "summary": "Overall emissions reduced by 8% compared to previous quarter."
    }

    return JsonResponse(data)


def pdf_report(request):
    data = {
        "status": "success",
        "report": "PDF Report Generation Successful"
    }

    return JsonResponse(data)
