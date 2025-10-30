from django.urls import path
from . import views
from .views import UserListAPI

from .views import room, create_room, list_rooms, room_detail, delete_room, create_device, list_devices, toggle_device

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('register/', register_view, name='register'),
    path('users/list/', UserListAPI.as_view(), name='user-list'),
    
    path('dashboard', views.dashboard, name='dashboard'),
    path('live', views.index, name='index'),
    path('video_feed/', views.video_feed, name='video_feed'),
    
    
    # room
    path('rooms', room, name='room'),
    path('rooms/create/', create_room, name="create-room"),
    path('rooms/list/', list_rooms, name="list-rooms"),
    path('rooms/<int:room_id>/', room_detail, name='room-detail'),
    path('rooms/<int:room_id>/delete/', delete_room, name='delete-room'),

    
    # devices
    path('devices/<int:room_id>/create/', create_device, name='create-device'),
    path('devices/<int:room_id>/', list_devices, name='list-devices'),
    path('devices/<int:device_id>/toggle/', toggle_device, name='toggle-device'),
]
