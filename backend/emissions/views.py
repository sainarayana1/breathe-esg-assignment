from django.db.models import Sum, Count
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from reportlab.pdfgen import canvas

from .models import EmissionRecord

from audits.models import AuditLog
from companies.models import Company


class ReviewEmissionView(APIView):

    def post(self, request, record_id):

        action = request.data.get("action")

        try:
            record = EmissionRecord.objects.get(id=record_id)

        except EmissionRecord.DoesNotExist:
            return Response({
                "error": "Emission record not found"
            }, status=404)

        # Review workflow
        if action == "approve":
            record.review_status = "approved"

        elif action == "reject":
            record.review_status = "rejected"

        else:
            return Response({
                "error": "Invalid action"
            }, status=400)

        record.save()

        # Audit logging
        AuditLog.objects.create(
            company=record.company,
            emission_record=record,
            action=record.review_status,
            actor="analyst_user",
            metadata={
                "category": record.category,
                "scope": record.scope,
                "quantity": record.quantity,
                "co2e": record.co2e
            }
        )

        return Response({
            "message": f"Record {action}d successfully",
            "record_id": record.id,
            "review_status": record.review_status
        })


class ESGDashboardView(APIView):

    def get(self, request):

        total_emissions = EmissionRecord.objects.aggregate(
            total=Sum("co2e")
        )

        scope1 = EmissionRecord.objects.filter(
            scope="scope_1"
        ).aggregate(total=Sum("co2e"))

        scope2 = EmissionRecord.objects.filter(
            scope="scope_2"
        ).aggregate(total=Sum("co2e"))

        scope3 = EmissionRecord.objects.filter(
            scope="scope_3"
        ).aggregate(total=Sum("co2e"))

        approved = EmissionRecord.objects.filter(
            review_status="approved"
        ).count()

        rejected = EmissionRecord.objects.filter(
            review_status="rejected"
        ).count()

        pending = EmissionRecord.objects.filter(
            review_status="pending"
        ).count()

        suspicious = EmissionRecord.objects.filter(
            quantity__lt=0
        ).count()

        return Response({

            "total_emissions": total_emissions["total"] or 0,

            "scope_1_emissions": scope1["total"] or 0,
            "scope_2_emissions": scope2["total"] or 0,
            "scope_3_emissions": scope3["total"] or 0,

            "approved_records": approved,
            "rejected_records": rejected,
            "pending_records": pending,

            "suspicious_records": suspicious
        })


class TopEmissionSourcesView(APIView):

    def get(self, request):

        top_sources = (
            EmissionRecord.objects
            .values("category")
            .annotate(total_co2e=Sum("co2e"))
            .order_by("-total_co2e")
        )

        return Response(top_sources)


class ESGAnalyticsView(APIView):

    def get(self, request):

        total_records = EmissionRecord.objects.count()

        total_emissions = EmissionRecord.objects.aggregate(
            total=Sum("co2e")
        )["total"] or 0

        avg_emission = 0

        if total_records > 0:
            avg_emission = total_emissions / total_records

        highest_record = (
            EmissionRecord.objects
            .order_by("-co2e")
            .first()
        )

        highest_data = {}

        if highest_record:
            highest_data = {
                "category": highest_record.category,
                "scope": highest_record.scope,
                "co2e": highest_record.co2e
            }

        return Response({
            "total_records": total_records,
            "total_emissions": total_emissions,
            "average_emission": avg_emission,
            "highest_emission_source": highest_data
        })


class ESGSummaryReportView(APIView):

    def get(self, request):

        total_emissions = EmissionRecord.objects.aggregate(
            total=Sum("co2e")
        )["total"] or 0

        total_records = EmissionRecord.objects.count()

        approved_records = EmissionRecord.objects.filter(
            review_status="approved"
        ).count()

        suspicious_records = EmissionRecord.objects.filter(
            quantity__lt=0
        ).count()

        scope1 = EmissionRecord.objects.filter(
            scope="scope_1"
        ).aggregate(total=Sum("co2e"))["total"] or 0

        scope2 = EmissionRecord.objects.filter(
            scope="scope_2"
        ).aggregate(total=Sum("co2e"))["total"] or 0

        scope3 = EmissionRecord.objects.filter(
            scope="scope_3"
        ).aggregate(total=Sum("co2e"))["total"] or 0

        return Response({

            "company": "Acme Manufacturing",

            "summary": {
                "total_records": total_records,
                "total_emissions": total_emissions,
                "approved_records": approved_records,
                "suspicious_records": suspicious_records
            },

            "scope_breakdown": {
                "scope_1": scope1,
                "scope_2": scope2,
                "scope_3": scope3
            },

            "status": "ESG reporting completed successfully"
        })


class ESGHealthScoreView(APIView):

    def get(self, request):

        total_records = EmissionRecord.objects.count()

        suspicious_records = EmissionRecord.objects.filter(
            quantity__lt=0
        ).count()

        approved_records = EmissionRecord.objects.filter(
            review_status="approved"
        ).count()

        health_score = 100

        health_score -= suspicious_records * 10
        health_score += approved_records * 2

        if health_score > 100:
            health_score = 100

        if health_score < 0:
            health_score = 0

        if health_score >= 80:
            status_label = "Excellent"

        elif health_score >= 60:
            status_label = "Good"

        elif health_score >= 40:
            status_label = "Moderate"

        else:
            status_label = "Poor"

        return Response({

            "company": "Acme Manufacturing",

            "health_score": health_score,

            "status": status_label,

            "details": {
                "total_records": total_records,
                "approved_records": approved_records,
                "suspicious_records": suspicious_records
            }
        })


class CompanyBenchmarkView(APIView):

    def get(self, request):

        companies = Company.objects.all()

        benchmark_data = []

        for company in companies:

            total_emissions = EmissionRecord.objects.filter(
                company=company
            ).aggregate(
                total=Sum("co2e")
            )["total"] or 0

            approved_records = EmissionRecord.objects.filter(
                company=company,
                review_status="approved"
            ).count()

            suspicious_records = EmissionRecord.objects.filter(
                company=company,
                quantity__lt=0
            ).count()

            benchmark_data.append({
                "company": company.name,
                "total_emissions": total_emissions,
                "approved_records": approved_records,
                "suspicious_records": suspicious_records
            })

        benchmark_data = sorted(
            benchmark_data,
            key=lambda x: x["total_emissions"]
        )

        return Response(benchmark_data)


class PDFReportView(APIView):

    def get(self, request):

        company = Company.objects.first()

        total_records = EmissionRecord.objects.count()

        total_emissions = (
            EmissionRecord.objects.aggregate(
                total=Sum("co2e")
            )["total"] or 0
        )

        approved_records = EmissionRecord.objects.filter(
            review_status="approved"
        ).count()

        suspicious_records = EmissionRecord.objects.filter(
            quantity__lt=0
        ).count()

        response = HttpResponse(
            content_type='application/pdf'
        )

        response['Content-Disposition'] = (
            'attachment; filename="esg_report.pdf"'
        )

        p = canvas.Canvas(response)

        # Title
        p.setFont("Helvetica-Bold", 24)
        p.drawString(140, 800, "ESG EMISSIONS REPORT")

        # Body
        p.setFont("Helvetica", 16)

        p.drawString(
            80,
            720,
            f"Company: {company.name}"
        )

        p.drawString(
            80,
            670,
            f"Total Records: {total_records}"
        )

        p.drawString(
            80,
            620,
            f"Total Emissions: {round(total_emissions, 2)}"
        )

        p.drawString(
            80,
            570,
            f"Approved Records: {approved_records}"
        )

        p.drawString(
            80,
            520,
            f"Suspicious Records: {suspicious_records}"
        )

        p.drawString(
            80,
            430,
            "Generated using ESG Analytics Platform"
        )

        p.showPage()
        p.save()

        return response