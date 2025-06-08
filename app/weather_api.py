import os
import requests

OWM_API_KEY = os.environ.get("OWM_API_KEY")  # Set this in your .env

def get_weather_and_forecast(geo):
    """
    geo: dict with keys 'lat', 'lon', 'display_name'
    Returns: (current_weather_dict, forecast_list)
    """
    if not OWM_API_KEY:
        raise Exception("OpenWeatherMap API key not set in OWM_API_KEY env var.")
    lat, lon = geo['lat'], geo['lon']

    # Current weather
    w_url = "https://api.openweathermap.org/data/2.5/weather"
    w_params = {"lat": lat, "lon": lon, "appid": OWM_API_KEY, "units": "metric"}
    w_resp = requests.get(w_url, params=w_params)
    w_resp.raise_for_status()
    weather = w_resp.json()

    # 5-day forecast (3-hour step)
    f_url = "https://api.openweathermap.org/data/2.5/forecast"
    f_params = {"lat": lat, "lon": lon, "appid": OWM_API_KEY, "units": "metric"}
    f_resp = requests.get(f_url, params=f_params)
    f_resp.raise_for_status()
    forecast = f_resp.json()

    return weather, forecast

