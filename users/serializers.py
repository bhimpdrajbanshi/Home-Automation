from rest_framework import serializers
from .models import Room, Device
from rest_framework.validators import UniqueValidator

class RoomSerializer(serializers.ModelSerializer):
    device_count = serializers.SerializerMethodField()
    class Meta:
        model = Room
        fields = ['id', 'name', "device_count"]
    def get_device_count(self, obj):
        return obj.devices.count()  # related_name="devices"
        
class DeviceSerializer(serializers.ModelSerializer):
    device_id = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=Device.objects.all(),
                message="Device with this Node MCU ESP Module pin ID already exists. Please use a different ID.."
            )
        ]
    )
    class Meta:
        model = Device
        fields = ['id', 'name', 'device_id', 'device_type', 'state', 'last_updated', 'room']
        read_only_fields = ['room', 'last_updated']

class RoomDetailSerializer(serializers.ModelSerializer):
    devices = DeviceSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'name', 'devices']
        
        
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
