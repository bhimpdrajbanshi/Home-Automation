from django.urls import path
from . import views

from .views import room, create_room, list_rooms, create_device, list_devices, toggle_device

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('register/', register_view, name='register'),
    
    path('dashboard', views.dashboard, name='dashboard'),
    path('live', views.index, name='index'),
    path('video_feed/', views.video_feed, name='video_feed'),
    
    
    # room
    path('rooms', room, name='room'),
    path('rooms/create/', create_room, name="create-room"),
    path('rooms/list/', list_rooms, name="list-rooms"),
    
    # devices
    path('devices/<int:room_id>/create/', create_device, name='create-device'),
    path('devices/<int:room_id>/', list_devices, name='list-devices'),
    path('devices/<int:device_id>/toggle/', toggle_device, name='toggle-device'),
]
