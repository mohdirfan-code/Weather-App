import requests

def get_air_quality(lat, lon, api_key):
    url = "http://api.openweathermap.org/data/2.5/air_pollution"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key
    }
    resp = requests.get(url, params=params, timeout=6)
    resp.raise_for_status()
    data = resp.json()
    # Extract AQI and pollutant details
    if data["list"]:
        aqi = data["list"][0]["main"]["aqi"]
        components = data["list"][0]["components"]
        return {
            "aqi": aqi,  # 1=Good, 2=Fair, 3=Moderate, 4=Poor, 5=Very Poor
            "components": components
        }
    return None