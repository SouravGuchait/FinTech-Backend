"""Initial migration for portfolios."""

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """Create the portfolio model."""

    initial = True

    dependencies = [
        ("entity", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Portfolio",
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
                ("name", models.CharField(max_length=255)),
                ("base_currency", models.CharField(max_length=8)),
                (
                    "entity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="portfolios",
                        to="entity.entity",
                    ),
                ),
            ],
            options={"ordering": ("name",)},
        ),
    ]
