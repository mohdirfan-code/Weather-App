import requests
from flask import current_app

def geocode_location(location_name, api_key):
    params = {"q": location_name, "limit": 1, "appid": api_key}
    resp = requests.get("https://api.openweathermap.org/geo/1.0/direct", params=params, timeout=10)
    resp.raise_for_status()
    results = resp.json()
    if not results:
        raise ValueError("Could not find location")
    return results[0]  # {lat, lon, name, country, ...}

def fetch_weather(lat, lon, api_key):
    params = {"lat": lat, "lon": lon, "units": "metric", "appid": api_key}
    resp = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()

def fetch_forecast(lat, lon, api_key):
    params = {"lat": lat, "lon": lon, "units": "metric", "appid": api_key}
    resp = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()