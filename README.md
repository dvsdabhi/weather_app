# 🌦️ Live Weather Dashboard - Gujarat Cities

This Django-based application fetches **live weather data** for multiple cities using the OpenWeatherMap API. It uses **Celery + RabbitMQ** for background tasks and **Django cache** for fast access. The frontend auto-refreshes every minute to keep weather updates live without manual page reloads.

---

## 🚀 Features

- Multiple city weather display (Surat, Ahmedabad, Rajkot, etc.)
- Data fetched every 1 minute using Celery beat
- Uses Django cache for smooth performance
- Beautiful UI cards per city
- JavaScript auto-refresh (no reload needed)

---

## 🧰 Tech Stack

- 🐍 Python 3.11+
- 🌐 Django 4.x
- 🕒 Celery 5.x
- 📬 RabbitMQ (as broker)
- 🧠 Django Cache (File-based or LocMem)
- 💅 HTML + CSS + JS (auto-refresh)

---

## 🔧 Installation Steps

### 1. Clone the project

```bash
git clone https://github.com/dvsdabhi/weather_app.git
cd "project_folder"
```

### 2. Create Virtual Environment

```bash
python -m venv env
source env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables
Create .env (or set manually in utils.py) for OpenWeatherMap API:
```bash
WEATHER_API_KEY=your_api_key_here
```
Get your API key from: https://openweathermap.org/api


### 🧠 Setup RabbitMQ (Windows)

Download & install Erlang from: https://www.erlang.org/downloads

Download & install RabbitMQ: https://www.rabbitmq.com/install-windows.html

## Start RabbitMQ server:

Open RabbitMQ Command Prompt as admin

### Run: 
```bash
rabbitmq-plugins enable rabbitmq_management
```

Check: http://localhost:15672

Login: guest / guest

## 🛠️ Run the Project

### Start Django Server

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Start Celery Worker
```bash
celery -A weather_project worker --loglevel=info --pool=solo
```

### Start Celery Beat (for periodic tasks)
```bash
celery -A weather_project beat --loglevel=info
```

## 🔁 Add Periodic Task (via Django Admin)

Open: http://127.0.0.1:8000/admin/

Go to Periodic Tasks

Add:

Task: weather.tasks.fetch_all_weather

Interval: every 1 minute

Name: Fetch Weather Every 1 Minute


