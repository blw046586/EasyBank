"""
ASGI config for BankingApp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/stable/howto/deployment/asgi/
"""

import os
pip install uvicorn # type: ignore
uvicorn BankingApp.asgi:application --host 0.0.0.0 --port 8000 # type: ignore
from django.core.asgi import get_asgi_application # type: ignore

# Set the default settings module for the 'django' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BankingApp.settings')

# Get the ASGI application for the project.
application = get_asgi_application()
