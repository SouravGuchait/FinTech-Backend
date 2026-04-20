"""APIView endpoints for portfolios."""

from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from portfolio.models import Portfolio
from portfolio.serializers import PortfolioSerializer


@method_decorator(csrf_exempt, name="dispatch")
class PortfolioListCreateAPIView(APIView):
    """List and create portfolios."""

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Return portfolios with optional entity/name filtering."""
        portfolios = Portfolio.objects.select_related("entity")
        entity = request.query_params.get("entity")
        name = request.query_params.get("name")
        if entity:
            portfolios = portfolios.filter(entity__name=entity)
        if name:
            portfolios = portfolios.filter(name__icontains=name)

        serializer = PortfolioSerializer(portfolios, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Create a portfolio."""
        serializer = PortfolioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@method_decorator(csrf_exempt, name="dispatch")
class PortfolioDetailAPIView(APIView):
    """Retrieve, update, and delete one portfolio by name."""

    permission_classes = [IsAuthenticated]

    def get_object(self, name):
        """Return a portfolio by name."""
        return get_object_or_404(Portfolio.objects.select_related("entity"), name=name)

    def get(self, request, name):
        """Return one portfolio."""
        serializer = PortfolioSerializer(self.get_object(name))
        return Response(serializer.data)

    def put(self, request, name):
        """Replace one portfolio."""
        serializer = PortfolioSerializer(self.get_object(name), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, name):
        """Partially update one portfolio."""
        serializer = PortfolioSerializer(self.get_object(name), data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, name):
        """Delete one portfolio."""
        self.get_object(name).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
