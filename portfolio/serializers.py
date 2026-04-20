"""Serializers for portfolio APIs."""

from rest_framework import serializers

from entity.models import Entity
from portfolio.models import Portfolio


class PortfolioSerializer(serializers.ModelSerializer):
    """Serialize portfolios."""

    entity_name = serializers.CharField(source="entity.name", read_only=True)
    entity = serializers.SlugRelatedField(
        queryset=Entity.objects.all(),
        slug_field="name",
    )

    class Meta:
        """Serializer metadata."""

        model = Portfolio
        fields = ("id", "name", "entity", "entity_name", "base_currency")
