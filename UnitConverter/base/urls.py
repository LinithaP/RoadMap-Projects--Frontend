from django.urls import path

from . import views

urlpatterns = [
    
    path('length', views.convert_length, name='convert_length'),
    path('weight', views.convert_weight, name='convert_weight'),
    path('temp', views.convert_temp, name='convert_temp'),
]