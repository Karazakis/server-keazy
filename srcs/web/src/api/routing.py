from django.urls import path
from consumers import DeviceConsumer

websocket_urlpatterns = [
    path('ws/device/<str:device_id>/', DeviceConsumer.as_asgi()),
]
