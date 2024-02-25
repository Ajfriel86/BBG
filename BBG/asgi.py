"""
ASGI config for BBG project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os  # Import os module

# Import get_asgi_application function from django.core.asgi
from django.core.asgi import get_asgi_application

# Set default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BBG.settings')

application = get_asgi_application()  # Get the ASGI application
