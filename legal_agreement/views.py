"""APIView endpoints for legal agreements."""

from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from legal_agreement.models import LegalAgreement
from legal_agreement.serializers import LegalAgreementSerializer


@method_decorator(csrf_exempt, name="dispatch")
class LegalAgreementListCreateAPIView(APIView):
    """List and create legal agreements."""

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Return legal agreements with optional relationship filters."""
        agreements = LegalAgreement.objects.select_related("entity", "counterparty", "ccp", "fcm")
        for field in ("entity", "counterparty", "ccp", "fcm"):
            value = request.query_params.get(field)
            if value:
                agreements = agreements.filter(**{field: value})

        name = request.query_params.get("name")
        if name:
            agreements = agreements.filter(agreement_name__icontains=name)

        is_active = request.query_params.get("is_active")
        if is_active is not None:
            agreements = agreements.filter(is_active=is_active.lower() in {"1", "true", "yes"})

        serializer = LegalAgreementSerializer(agreements, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Create a legal agreement."""
        serializer = LegalAgreementSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@method_decorator(csrf_exempt, name="dispatch")
class LegalAgreementDetailAPIView(APIView):
    """Retrieve, update, and delete one legal agreement by name."""

    permission_classes = [IsAuthenticated]

    def get_object(self, name):
        """Return a legal agreement by name."""
        return get_object_or_404(
            LegalAgreement.objects.select_related("entity", "counterparty", "ccp", "fcm"),
            agreement_name=name,
        )

    def get(self, request, name):
        """Return one legal agreement."""
        serializer = LegalAgreementSerializer(self.get_object(name))
        return Response(serializer.data)

    def put(self, request, name):
        """Replace one legal agreement."""
        serializer = LegalAgreementSerializer(self.get_object(name), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, name):
        """Partially update one legal agreement."""
        serializer = LegalAgreementSerializer(self.get_object(name), data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, name):
        """Delete one legal agreement."""
        self.get_object(name).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
