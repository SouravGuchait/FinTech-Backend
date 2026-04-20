"""APIView endpoints for CCPs."""

from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ccp.models import CCP
from ccp.serializers import CCPSerializer


@method_decorator(csrf_exempt, name="dispatch")
class CCPListCreateAPIView(APIView):
    """List and create CCPs."""

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Return CCPs with optional entity/name filtering."""
        ccps = CCP.objects.select_related("entity")
        entity = request.query_params.get("entity")
        name = request.query_params.get("name")
        if entity:
            ccps = ccps.filter(entity__name=entity)
        if name:
            ccps = ccps.filter(name__icontains=name)

        serializer = CCPSerializer(ccps, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Create a CCP."""
        serializer = CCPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@method_decorator(csrf_exempt, name="dispatch")
class CCPDetailAPIView(APIView):
    """Retrieve, update, and delete one CCP by name."""

    permission_classes = [IsAuthenticated]

    def get_object(self, name):
        """Return a CCP by name."""
        return get_object_or_404(CCP.objects.select_related("entity"), name=name)

    def get(self, request, name):
        """Return one CCP."""
        serializer = CCPSerializer(self.get_object(name))
        return Response(serializer.data)

    def put(self, request, name):
        """Replace one CCP."""
        serializer = CCPSerializer(self.get_object(name), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, name):
        """Partially update one CCP."""
        serializer = CCPSerializer(self.get_object(name), data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, name):
        """Delete one CCP."""
        self.get_object(name).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
