from django.db import models

from companies.models import Company
from emissions.models import EmissionRecord


class AuditLog(models.Model):

    ACTION_CHOICES = [
        ("approved", "Approved"),
        ("rejected", "Rejected"),
        ("uploaded", "Uploaded"),
    ]

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )

    emission_record = models.ForeignKey(
        EmissionRecord,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    action = models.CharField(
        max_length=50,
        choices=ACTION_CHOICES
    )

    actor = models.CharField(
        max_length=255,
        default="system"
    )

    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    metadata = models.JSONField(
        default=dict
    )

    def __str__(self):
        return f"{self.company.name} - {self.action}"