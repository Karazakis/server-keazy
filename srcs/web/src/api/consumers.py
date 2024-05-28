import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Device
from asgiref.sync import database_sync_to_async

class DeviceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.device_id = self.scope['url_route']['kwargs']['device_id']
        self.device_group_name = f'device_{self.device_id}'

        # Set device online status
        await self.set_device_status(online=True)

        await self.channel_layer.group_add(
            self.device_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Set device offline status
        await self.set_device_status(online=False)

        await self.channel_layer.group_discard(
            self.device_group_name,
            self.channel_name
        )

    @database_sync_to_async
    def set_device_status(self, online):
        device = Device.objects.get(device_id=self.device_id)
        device.is_online = online
        device.save()
