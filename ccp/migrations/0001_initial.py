"""Initial migration for CCPs."""

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """Create the CCP model."""

    initial = True

    dependencies = [
        ("entity", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CCP",
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
                (
                    "entity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ccps",
                        to="entity.entity",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
                "verbose_name": "CCP",
                "verbose_name_plural": "CCPs",
            },
        ),
    ]
