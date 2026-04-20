"""Serializers for CCP APIs."""

from rest_framework import serializers

from ccp.models import CCP
from entity.models import Entity


class CCPSerializer(serializers.ModelSerializer):
    """Serialize CCPs."""

    entity_name = serializers.CharField(source="entity.name", read_only=True)
    entity = serializers.SlugRelatedField(
        queryset=Entity.objects.all(),
        slug_field="name",
    )

    class Meta:
        """Serializer metadata."""

        model = CCP
        fields = ("id", "name", "entity", "entity_name")
