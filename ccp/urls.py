"""CCP app routes."""

from django.urls import path

from ccp.views import CCPDetailAPIView, CCPListCreateAPIView

urlpatterns = [
    path("", CCPListCreateAPIView.as_view(), name="ccp-list-create"),
    path("<str:name>/", CCPDetailAPIView.as_view(), name="ccp-detail"),
]
