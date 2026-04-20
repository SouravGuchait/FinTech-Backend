"""Counterparty app routes."""

from django.urls import path

from counterparty.views import CounterpartyDetailAPIView, CounterpartyListCreateAPIView

urlpatterns = [
    path("", CounterpartyListCreateAPIView.as_view(), name="counterparty-list-create"),
    path("<str:name>/", CounterpartyDetailAPIView.as_view(), name="counterparty-detail"),
]
