import requests

def resolve_location(location_str):
    """
    Resolve user input (zip, city, landmark, coords) to lat/lon using OSM Nominatim API.
    Returns dict: {'lat': float, 'lon': float, 'display_name': str} or None.
    """
    if not location_str:
        return None
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": location_str, "format": "json", "limit": 1}
    resp = requests.get(url, params=params, headers={"User-Agent": "WeatherApp/1.0"})
    resp.raise_for_status()
    data = resp.json()
    if not data:
        return None
    res = data[0]
    return {"lat": float(res["lat"]), "lon": float(res["lon"]), "display_name": res["display_name"]}