from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

class User(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username
    
class Room(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rooms")
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.user.username})"

class Device(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="devices")
    name = models.CharField(max_length=50)
    device_id = models.CharField(max_length=100, unique=True)  # Unique ESP ID
    device_type = models.CharField(max_length=30, default='switch')  # light, fan, etc.
    state = models.BooleanField(default=False)  # On/Off
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} [{self.device_id}]"