"""Serializers for entity APIs."""

from rest_framework import serializers

from entity.models import Entity


class EntitySerializer(serializers.ModelSerializer):
    """Serialize entities."""

    created_by_email = serializers.EmailField(source="created_by.email", read_only=True)

    class Meta:
        """Serializer metadata."""

        model = Entity
        fields = ("id", "name", "entity_type", "created_by", "created_by_email")
        read_only_fields = ("created_by",)
