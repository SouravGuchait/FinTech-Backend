"""URL configuration for the trade platform backend."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("user.urls")),
    path("api/entities/", include("entity.urls")),
    path("api/portfolios/", include("portfolio.urls")),
    path("api/counterparties/", include("counterparty.urls")),
    path("api/ccps/", include("ccp.urls")),
    path("api/fcms/", include("fcm.urls")),
    path("api/legal-agreements/", include("legal_agreement.urls")),
]
