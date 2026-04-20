"""Legal agreement model."""

from datetime import timedelta

from django.db import models
from django.utils import timezone

from ccp.models import CCP
from counterparty.models import Counterparty
from entity.models import Entity
from fcm.models import FCM


def default_end_date():
    """Return a default agreement end date one year from today."""
    return timezone.now().date() + timedelta(days=365)


class LegalAgreement(models.Model):
    """Legal agreement between entity, counterparty, CCP, and FCM."""

    agreement_name = models.CharField(max_length=255)
    entity = models.OneToOneField(
        Entity,
        on_delete=models.CASCADE,
        related_name="legal_agreement",
    )
    counterparty = models.ForeignKey(
        Counterparty,
        on_delete=models.CASCADE,
        related_name="legal_agreements",
    )
    ccp = models.ForeignKey(
        CCP,
        on_delete=models.CASCADE,
        related_name="legal_agreements",
    )
    fcm = models.OneToOneField(
        FCM,
        on_delete=models.CASCADE,
        related_name="legal_agreement",
    )
    agreement_type = models.CharField(max_length=64)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(default=default_end_date)
    is_active = models.BooleanField(default=True)

    objects = models.Manager()

    class Meta:
        """Model metadata."""

        ordering = ("agreement_name",)

    def __str__(self) -> str:
        """Return the agreement name."""
        return str(self.agreement_name)
