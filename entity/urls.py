"""Entity app routes."""

from django.urls import path

from entity.views import EntityDetailAPIView, EntityListCreateAPIView

urlpatterns = [
    path("", EntityListCreateAPIView.as_view(), name="entity-list-create"),
    path("<str:name>/", EntityDetailAPIView.as_view(), name="entity-detail"),
]
