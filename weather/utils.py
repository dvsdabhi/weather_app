import requests

def get_weather(city):
    API_KEY = 'ENTER YOUR API KEY'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
    else:
        return None
