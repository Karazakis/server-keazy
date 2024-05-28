from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='api_users',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='api_users_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )


class Device(models.Model):
    name = models.CharField(max_length=100)
    device_id = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100)
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Keazy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='keazies')
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='keazies')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.device.name}"