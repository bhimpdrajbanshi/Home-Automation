from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from users.models import Room, Device
from users.serializers import DeviceSerializer

# Create Device
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_device(request, room_id):
    try:
        room = Room.objects.get(id=room_id, user=request.user)
    except Room.DoesNotExist:
        return Response({"error": "Room not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = DeviceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(room=room)
        return Response({"message": "Device created", "device": serializer.data}, status=status.HTTP_201_CREATED)
    return Response( {"error": serializer.errors }, status=status.HTTP_400_BAD_REQUEST)

# List devices in a room
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_devices(request, room_id):
    try:
        room = Room.objects.get(id=room_id, user=request.user)
    except Room.DoesNotExist:
        return Response({"error": "Room not found"}, status=status.HTTP_404_NOT_FOUND)

    devices = room.devices.all()
    serializer = DeviceSerializer(devices, many=True)
    return Response(serializer.data)

# Toggle device state
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def toggle_device(request, device_id):
    try:
        device = Device.objects.get(id=device_id, room__user=request.user)
    except Device.DoesNotExist:
        return Response({"error": "Device not found"}, status=status.HTTP_404_NOT_FOUND)

    device.state = not device.state
    device.save()
    serializer = DeviceSerializer(device)
    return Response({"message": "Device state updated", "device": serializer.data})
