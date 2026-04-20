"""Serializers for FCM APIs."""

from rest_framework import serializers

from entity.models import Entity
from fcm.models import FCM


class FCMSerializer(serializers.ModelSerializer):
    """Serialize FCMs."""

    entity_name = serializers.CharField(source="entity.name", read_only=True)
    entity = serializers.SlugRelatedField(
        queryset=Entity.objects.all(),
        slug_field="name",
    )

    class Meta:
        """Serializer metadata."""

        model = FCM
        fields = ("id", "name", "entity", "entity_name")
