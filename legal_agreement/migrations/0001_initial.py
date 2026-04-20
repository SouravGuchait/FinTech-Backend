"""Initial migration for legal agreements."""

from django.db import migrations, models
import django.db.models.deletion
import legal_agreement.models


class Migration(migrations.Migration):
    """Create the legal agreement model."""

    initial = True

    dependencies = [
        ("ccp", "0001_initial"),
        ("counterparty", "0001_initial"),
        ("entity", "0001_initial"),
        ("fcm", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="LegalAgreement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("agreement_name", models.CharField(max_length=255)),
                ("agreement_type", models.CharField(max_length=64)),
                ("start_date", models.DateField(auto_now_add=True)),
                ("end_date", models.DateField(default=legal_agreement.models.default_end_date)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "ccp",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="legal_agreements",
                        to="ccp.ccp",
                    ),
                ),
                (
                    "counterparty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="legal_agreements",
                        to="counterparty.counterparty",
                    ),
                ),
                (
                    "entity",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="legal_agreement",
                        to="entity.entity",
                    ),
                ),
                (
                    "fcm",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="legal_agreement",
                        to="fcm.fcm",
                    ),
                ),
            ],
            options={"ordering": ("agreement_name",)},
        ),
    ]
