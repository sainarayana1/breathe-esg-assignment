from django.db import models
from companies.models import Company

class DataSource(models.Model):

    SOURCE_TYPES = [
        ("sap", "SAP"),
        ("utility", "Utility"),
        ("travel", "Travel"),
    ]

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )

    source_type = models.CharField(
        max_length=50,
        choices=SOURCE_TYPES
    )

    upload_name = models.CharField(max_length=255)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company.name} - {self.source_type}"
class RawRecord(models.Model):

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("valid", "Valid"),
        ("failed", "Failed"),
        ("suspicious", "Suspicious"),
    ]

    data_source = models.ForeignKey(
        DataSource,
        on_delete=models.CASCADE
    )

    raw_data = models.JSONField()

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="pending"
    )

    validation_errors = models.JSONField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)