from django.urls import path
from . import views

urlpatterns = [
    path('', views.aaa, name='dashboardss'),
    path('status/', views.get_status, name='get_status'),
    path('control/', views.control_bulb, name='control_bulb'),  # new API
]
