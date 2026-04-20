"""Serializers for counterparty APIs."""

from rest_framework import serializers

from counterparty.models import Counterparty


class CounterpartySerializer(serializers.ModelSerializer):
    """Serialize counterparties."""

    class Meta:
        """Serializer metadata."""

        model = Counterparty
        fields = ("id", "name", "counterparty_code")
