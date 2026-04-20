"""Legal agreement app routes."""

from django.urls import path

from legal_agreement.views import LegalAgreementDetailAPIView, LegalAgreementListCreateAPIView

urlpatterns = [
    path("", LegalAgreementListCreateAPIView.as_view(), name="legal-agreement-list-create"),
    path("<str:name>/", LegalAgreementDetailAPIView.as_view(), name="legal-agreement-detail"),
]
