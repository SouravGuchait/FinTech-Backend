"""APIView endpoints for counterparties."""

from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from counterparty.models import Counterparty
from counterparty.serializers import CounterpartySerializer


@method_decorator(csrf_exempt, name="dispatch")
class CounterpartyListCreateAPIView(APIView):
    """List and create counterparties."""

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Return counterparties with optional name/code filtering."""
        counterparties = Counterparty.objects.all()
        name = request.query_params.get("name")
        code = request.query_params.get("counterparty_code")
        if name:
            counterparties = counterparties.filter(name__icontains=name)
        if code:
            counterparties = counterparties.filter(counterparty_code=code)

        serializer = CounterpartySerializer(counterparties, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Create a counterparty."""
        serializer = CounterpartySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@method_decorator(csrf_exempt, name="dispatch")
class CounterpartyDetailAPIView(APIView):
    """Retrieve, update, and delete one counterparty by name."""

    permission_classes = [IsAuthenticated]

    def get_object(self, name):
        """Return a counterparty by name."""
        return get_object_or_404(Counterparty, name=name)

    def get(self, request, name):
        """Return one counterparty."""
        serializer = CounterpartySerializer(self.get_object(name))
        return Response(serializer.data)

    def put(self, request, name):
        """Replace one counterparty."""
        serializer = CounterpartySerializer(self.get_object(name), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, name):
        """Partially update one counterparty."""
        serializer = CounterpartySerializer(self.get_object(name), data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, name):
        """Delete one counterparty."""
        self.get_object(name).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
