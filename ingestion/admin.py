from django.contrib import admin
from .models import DataSource, RawRecord


@admin.register(DataSource)
class DataSourceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "company",
        "source_type",
        "upload_name",
        "uploaded_at",
    )


@admin.register(RawRecord)
class RawRecordAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "data_source",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
    )

    search_fields = (
        "status",
    )