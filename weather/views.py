from django.shortcuts import render
from django.core.cache import cache
from django.core.cache import caches
from django.http import HttpResponse, JsonResponse
from django.conf import settings
import os

# Create your views here.

# def home(request):
#     data = cache.get('weather_data', {'temperature': 'N/A', 'description': 'N/A'})
#     print("Data:", data)
#     return render(request, 'weather/home.html', {'weather': data})

# from django.core.cache import cache
# from django.shortcuts import render

def home(request):
    data = cache.get('weather_data_all', {})
    return render(request, 'weather/home.html', {'weather_data': data})

# check only for cache value set or not set
def check_cache_view(request):
    print("cache.get('weather_data')",cache.get('weather_data'))
    data = cache.get('weather_data_all')
    print("Cache path:", os.path.join(settings.BASE_DIR, "weather_cache"))
    print("Data:", data)
    if data:
        message = "Cache is working"
    else:
        message = "Cache is empty"
    return HttpResponse(message)

def get_weather_json(request):
    data = cache.get('weather_data_all', {})
    return JsonResponse(data)
