from django.contrib import admin
from .models import User, Device, Keazy

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'device_id', 'location']

@admin.register(Keazy)
class KeazyAdmin(admin.ModelAdmin):
    list_display = ['user', 'device', 'created_at']