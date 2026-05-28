from django.contrib import admin
from .models import EmissionRecord


@admin.register(EmissionRecord)
class EmissionRecordAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "company",
        "scope",
        "category",
        "quantity",
        "normalized_unit",
        "co2e",
        "review_status",
        "locked_for_audit",
    )

    list_filter = (
        "scope",
        "review_status",
    )

    search_fields = (
        "category",
    )