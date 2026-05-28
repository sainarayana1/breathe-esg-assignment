from rest_framework.views import APIView
from rest_framework.response import Response

from .models import AuditLog


class AuditLogListView(APIView):

    def get(self, request):

        logs = AuditLog.objects.all().order_by("-timestamp")

        data = []

        for log in logs:

            data.append({
                "company": log.company.name,
                "emission_record_id": log.emission_record.id,
                "action": log.action,
                "actor": log.actor,
                "timestamp": log.timestamp,
                "metadata": log.metadata
            })

        return Response(data)