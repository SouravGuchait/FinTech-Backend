"""APIView endpoints for entities."""

from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from entity.models import Entity
from entity.serializers import EntitySerializer


@method_decorator(csrf_exempt, name="dispatch")
class EntityListCreateAPIView(APIView):
    """List and create entities."""

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Return entities with optional type/name filtering."""
        entities = Entity.objects.select_related("created_by")
        entity_type = request.query_params.get("entity_type")
        name = request.query_params.get("name")
        if entity_type:
            entities = entities.filter(entity_type=entity_type)
        if name:
            entities = entities.filter(name__icontains=name)

        serializer = EntitySerializer(entities, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Create an entity owned by the current session user."""
        serializer = EntitySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@method_decorator(csrf_exempt, name="dispatch")
class EntityDetailAPIView(APIView):
    """Retrieve, update, and delete one entity by name."""

    permission_classes = [IsAuthenticated]

    def get_object(self, name):
        """Return an entity by name."""
        return get_object_or_404(Entity.objects.select_related("created_by"), name=name)

    def get(self, request, name):
        """Return one entity."""
        serializer = EntitySerializer(self.get_object(name))
        return Response(serializer.data)

    def put(self, request, name):
        """Replace one entity."""
        entity = self.get_object(name)
        serializer = EntitySerializer(entity, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=entity.created_by)
        return Response(serializer.data)

    def patch(self, request, name):
        """Partially update one entity."""
        entity = self.get_object(name)
        serializer = EntitySerializer(entity, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=entity.created_by)
        return Response(serializer.data)

    def delete(self, request, name):
        """Delete one entity."""
        self.get_object(name).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
