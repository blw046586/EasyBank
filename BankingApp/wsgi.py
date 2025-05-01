"""
WSGI config for BankingApp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/stable/howto/deployment/wsgi/
"""

import os
pip install gunicorn # type: ignore
gunicorn BankingApp.wsgi:application --bind 0.0.0.0:8000 # type: ignore
from django.core.wsgi import get_wsgi_application # type: ignore

# Set the default settings module for the 'django' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BankingApp.settings')

# Get the WSGI application for the project.
application = get_wsgi_application()
