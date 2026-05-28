import pandas as pd

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CSVUploadSerializer
from .models import DataSource, RawRecord

from companies.models import Company
from emissions.models import EmissionRecord


# =========================================================
# SAP FUEL INGESTION (SCOPE 1)
# =========================================================

class SAPUploadView(APIView):

    def post(self, request):

        serializer = CSVUploadSerializer(data=request.data)

        if serializer.is_valid():

            file = serializer.validated_data["file"]
            company_id = serializer.validated_data["company_id"]

            company = Company.objects.get(id=company_id)

            # Create datasource
            data_source = DataSource.objects.create(
                company=company,
                source_type="sap",
                upload_name=file.name
            )

            # Read CSV
            df = pd.read_csv(file)

            processed = 0

            for _, row in df.iterrows():

                # Store raw data
                raw_record = RawRecord.objects.create(
                    data_source=data_source,
                    raw_data=row.to_dict()
                )

                quantity = row["Quantity"]

                status_value = "valid"
                errors = []

                # Validation
                if quantity < 0:
                    status_value = "suspicious"
                    errors.append("Negative fuel quantity")

                raw_record.status = status_value
                raw_record.validation_errors = errors
                raw_record.save()

                # Emission factor for fuel
                co2e = quantity * 2.68

                # Create normalized emission record
                EmissionRecord.objects.create(
                    company=company,
                    raw_record=raw_record,
                    scope="scope_1",
                    category=row["Fuel_Type"],
                    quantity=quantity,
                    normalized_unit=row["Unit"],
                    co2e=co2e
                )

                processed += 1

            return Response({
                "message": "SAP CSV ingested successfully",
                "rows_processed": processed
            })

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# =========================================================
# UTILITY ELECTRICITY INGESTION (SCOPE 2)
# =========================================================

class UtilityUploadView(APIView):

    def post(self, request):

        serializer = CSVUploadSerializer(data=request.data)

        if serializer.is_valid():

            file = serializer.validated_data["file"]
            company_id = serializer.validated_data["company_id"]

            company = Company.objects.get(id=company_id)

            # Create datasource
            data_source = DataSource.objects.create(
                company=company,
                source_type="utility",
                upload_name=file.name
            )

            # Read CSV
            df = pd.read_csv(file)

            processed = 0

            for _, row in df.iterrows():

                # Store raw data
                raw_record = RawRecord.objects.create(
                    data_source=data_source,
                    raw_data=row.to_dict()
                )

                kwh = row["kWh"]

                status_value = "valid"
                errors = []

                # Validation
                if kwh < 0:
                    status_value = "suspicious"
                    errors.append("Negative electricity usage")

                raw_record.status = status_value
                raw_record.validation_errors = errors
                raw_record.save()

                # Electricity emission factor
                co2e = kwh * 0.82

                # Create emission record
                EmissionRecord.objects.create(
                    company=company,
                    raw_record=raw_record,
                    scope="scope_2",
                    category="Electricity",
                    quantity=kwh,
                    normalized_unit=row["Unit"],
                    co2e=co2e
                )

                processed += 1

            return Response({
                "message": "Utility CSV ingested successfully",
                "rows_processed": processed
            })

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# =========================================================
# CORPORATE TRAVEL INGESTION (SCOPE 3)
# =========================================================

class TravelUploadView(APIView):

    def post(self, request):

        serializer = CSVUploadSerializer(data=request.data)

        if serializer.is_valid():

            file = serializer.validated_data["file"]
            company_id = serializer.validated_data["company_id"]

            company = Company.objects.get(id=company_id)

            # Create datasource
            data_source = DataSource.objects.create(
                company=company,
                source_type="travel",
                upload_name=file.name
            )

            # Read CSV
            df = pd.read_csv(file)

            processed = 0

            for _, row in df.iterrows():

                # Store raw data
                raw_record = RawRecord.objects.create(
                    data_source=data_source,
                    raw_data=row.to_dict()
                )

                distance = row["Distance_km"]

                status_value = "valid"
                errors = []

                # Validation
                if distance < 0:
                    status_value = "suspicious"
                    errors.append("Negative travel distance")

                raw_record.status = status_value
                raw_record.validation_errors = errors
                raw_record.save()

                travel_type = row["Travel_Type"]

                # Emission factors
                if travel_type == "Flight":
                    factor = 0.115

                elif travel_type == "Train":
                    factor = 0.041

                else:
                    factor = 0.05

                # CO2 calculation
                co2e = distance * factor

                # Create emission record
                EmissionRecord.objects.create(
                    company=company,
                    raw_record=raw_record,
                    scope="scope_3",
                    category=travel_type,
                    quantity=distance,
                    normalized_unit="km",
                    co2e=co2e
                )

                processed += 1

            return Response({
                "message": "Travel CSV ingested successfully",
                "rows_processed": processed
            })

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )