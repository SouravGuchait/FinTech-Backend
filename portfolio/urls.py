"""Portfolio app routes."""

from django.urls import path

from portfolio.views import PortfolioDetailAPIView, PortfolioListCreateAPIView

urlpatterns = [
    path("", PortfolioListCreateAPIView.as_view(), name="portfolio-list-create"),
    path("<str:name>/", PortfolioDetailAPIView.as_view(), name="portfolio-detail"),
]
