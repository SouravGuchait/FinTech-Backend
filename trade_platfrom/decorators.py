"""Decorators for the trade platform."""

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


def csrf_exempt_decorator(view_class):
    """Apply CSRF exemption to all HTTP methods of a class-based view."""
    return method_decorator(csrf_exempt, name="dispatch")(view_class)
