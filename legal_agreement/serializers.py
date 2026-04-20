"""Serializers for legal agreement APIs."""

from rest_framework import serializers

from ccp.models import CCP
from counterparty.models import Counterparty
from entity.models import Entity
from fcm.models import FCM
from legal_agreement.models import LegalAgreement


class LegalAgreementSerializer(serializers.ModelSerializer):
    """Serialize legal agreements."""

    entity_name = serializers.CharField(source="entity.name", read_only=True)
    counterparty_name = serializers.CharField(source="counterparty.name", read_only=True)
    ccp_name = serializers.CharField(source="ccp.name", read_only=True)
    fcm_name = serializers.CharField(source="fcm.name", read_only=True)
    entity = serializers.SlugRelatedField(
        queryset=Entity.objects.all(),
        slug_field="name",
    )
    counterparty = serializers.SlugRelatedField(
        queryset=Counterparty.objects.all(),
        slug_field="name",
    )
    ccp = serializers.SlugRelatedField(
        queryset=CCP.objects.all(),
        slug_field="name",
    )
    fcm = serializers.SlugRelatedField(
        queryset=FCM.objects.all(),
        slug_field="name",
    )

    class Meta:
        """Serializer metadata."""

        model = LegalAgreement
        fields = (
            "id",
            "agreement_name",
            "entity",
            "entity_name",
            "counterparty",
            "counterparty_name",
            "ccp",
            "ccp_name",
            "fcm",
            "fcm_name",
            "agreement_type",
            "start_date",
            "end_date",
            "is_active",
        )
        read_only_fields = ("start_date", "end_date")
