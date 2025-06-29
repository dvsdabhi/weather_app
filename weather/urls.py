from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('check-cache/', views.check_cache_view),
    path('weather-json/', views.get_weather_json, name='weather_json'),
]
