"""
ASGI config for pos project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""
# pos/asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import kiosk.routing  # Thay 'kiosk' bằng tên của ứng dụng Django của bạn

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pos.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            kiosk.routing.websocket_urlpatterns
        )
    ),
})
