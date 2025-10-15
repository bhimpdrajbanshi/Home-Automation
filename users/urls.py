from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('register/', register_view, name='register'),
    
    path('dashboard', views.dashboard, name='dashboard'),
    path('live', views.index, name='index'),
    path('video_feed/', views.video_feed, name='video_feed'),
]
