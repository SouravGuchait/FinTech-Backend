"""Initial migration for counterparties."""

from django.db import migrations, models


class Migration(migrations.Migration):
    """Create the counterparty model."""

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Counterparty",
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
                ("counterparty_code", models.CharField(max_length=64, unique=True)),
            ],
            options={"ordering": ("name",), "verbose_name_plural": "counterparties"},
        ),
    ]
