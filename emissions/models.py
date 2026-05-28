from django.db import models
from companies.models import Company
from ingestion.models import RawRecord

class EmissionRecord(models.Model):

    SCOPE_CHOICES = [
        ("scope_1", "Scope 1"),
        ("scope_2", "Scope 2"),
        ("scope_3", "Scope 3"),
    ]

    REVIEW_STATUS = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )

    raw_record = models.ForeignKey(
        RawRecord,
        on_delete=models.CASCADE
    )

    scope = models.CharField(
        max_length=50,
        choices=SCOPE_CHOICES
    )

    category = models.CharField(max_length=255)

    quantity = models.FloatField()

    normalized_unit = models.CharField(max_length=50)

    co2e = models.FloatField()

    review_status = models.CharField(
        max_length=50,
        choices=REVIEW_STATUS,
        default="pending"
    )

    locked_for_audit = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)