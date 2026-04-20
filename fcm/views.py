"""APIView endpoints for FCMs."""

from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from fcm.models import FCM
from fcm.serializers import FCMSerializer


@method_decorator(csrf_exempt, name="dispatch")
class FCMListCreateAPIView(APIView):
    """List and create FCMs."""

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Return FCMs with optional entity/name filtering."""
        fcms = FCM.objects.select_related("entity")
        entity = request.query_params.get("entity")
        name = request.query_params.get("name")
        if entity:
            fcms = fcms.filter(entity__name=entity)
        if name:
            fcms = fcms.filter(name__icontains=name)

        serializer = FCMSerializer(fcms, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Create an FCM."""
        serializer = FCMSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@method_decorator(csrf_exempt, name="dispatch")
class FCMDetailAPIView(APIView):
    """Retrieve, update, and delete one FCM by name."""

    permission_classes = [IsAuthenticated]

    def get_object(self, name):
        """Return an FCM by name."""
        return get_object_or_404(FCM.objects.select_related("entity"), name=name)

    def get(self, request, name):
        """Return one FCM."""
        serializer = FCMSerializer(self.get_object(name))
        return Response(serializer.data)

    def put(self, request, name):
        """Replace one FCM."""
        serializer = FCMSerializer(self.get_object(name), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, name):
        """Partially update one FCM."""
        serializer = FCMSerializer(self.get_object(name), data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, name):
        """Delete one FCM."""
        self.get_object(name).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
