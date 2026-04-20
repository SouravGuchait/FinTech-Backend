"""WSGI config for trade_platfrom project."""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trade_platfrom.settings")

application = get_wsgi_application()
