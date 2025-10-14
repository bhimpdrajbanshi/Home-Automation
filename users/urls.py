from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('live', views.index, name='index'),
    path('video_feed/', views.video_feed, name='video_feed'),
]
