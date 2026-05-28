from django.urls import path

from .views import (
    SAPUploadView,
    UtilityUploadView,
    TravelUploadView,
)

urlpatterns = [

    # SAP Upload
    path(
        "upload/sap/",
        SAPUploadView.as_view()
    ),

    # Utility Upload
    path(
        "upload/utility/",
        UtilityUploadView.as_view()
    ),

    # Travel Upload
    path(
        "upload/travel/",
        TravelUploadView.as_view()
    ),
]