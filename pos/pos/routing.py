# routing.py
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
import kiosk.routing  # Thay your_app bằng tên ứng dụng của bạn

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    "http": get_asgi_application(),  # Cấu hình cho Django HTTP views

    # WebSocket protocol handler
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                kiosk.routing.websocket_urlpatterns  # Định nghĩa URL cho WebSocket trong your_app
            )
        ),
    ),
})
