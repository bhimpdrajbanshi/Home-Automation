from rest_framework import serializers
from .models import Room, Device

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name']
        
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'name', 'device_id', 'device_type', 'state', 'last_updated', 'room']
        read_only_fields = ['room', 'last_updated']

class RoomDetailSerializer(serializers.ModelSerializer):
    devices = DeviceSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'name', 'devices']