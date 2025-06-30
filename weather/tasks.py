from celery import shared_task
from django.core.cache import cache
from .utils import get_weather

@shared_task
def fetch_weather_data():
    cities = ['Surat', 'Ahmedabad', 'Rajkot', 'Vadodara','Dwarka']
    weather_data = {}

    for city in cities:
        try:
            data = get_weather(city)
            weather_data[city] = data
        except Exception as e:
            print(f"Failed to fetch for {city}: {e}")
            weather_data[city] = {'temperature': 'N/A', 'description': 'N/A'}

    cache.set('weather_data_all', weather_data, timeout=60*5)
    print("All cities weather cached successfully")
