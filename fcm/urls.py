"""FCM app routes."""

from django.urls import path

from fcm.views import FCMDetailAPIView, FCMListCreateAPIView

urlpatterns = [
    path("", FCMListCreateAPIView.as_view(), name="fcm-list-create"),
    path("<str:name>/", FCMDetailAPIView.as_view(), name="fcm-detail"),
]
