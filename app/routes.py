import json
import os
import requests
import csv
import io
import xml.etree.ElementTree as ET
import markdown
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from .models import db, WeatherRecord
from .youtube_api import search_youtube_videos
from datetime import datetime
from .air_quality import get_air_quality
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from flask import Response, send_file, make_response

main_bp = Blueprint("main", __name__)

def get_owm_api_key():
    # Try environment variable first, then Flask config
    return os.environ.get("OWM_API_KEY") or current_app.config.get("OWM_API_KEY")

def geocode_location(location_name, api_key):
    """Geocode a location input to (lat, lon, name, country) using OWM's geo endpoint."""
    params = {"q": location_name, "limit": 1, "appid": api_key}
    resp = requests.get("https://api.openweathermap.org/geo/1.0/direct", params=params, timeout=10)
    resp.raise_for_status()
    results = resp.json()
    if not results:
        raise ValueError(f"Could not find location: {location_name}")
    return results[0]  # {lat, lon, name, country, ...}

def fetch_weather(lat, lon, api_key):
    """Fetch current weather for coordinates."""
    params = {"lat": lat, "lon": lon, "units": "metric", "appid": api_key}
    resp = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()

def fetch_forecast(lat, lon, api_key):
    """Fetch 5-day/3-hour forecast for coordinates."""
    params = {"lat": lat, "lon": lon, "units": "metric", "appid": api_key}
    resp = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()

@main_bp.route("/", methods=["GET", "POST"])
def index():
    weather = forecast = error = location = None
    lat = lon = None
    air_quality = None
    youtube_videos = []
    map_url = None

    if request.method == "POST":
        location = request.form.get("location", "").strip()
        api_key = get_owm_api_key()
        youtube_api_key = os.getenv("YOUTUBE_API_KEY") or current_app.config.get("YOUTUBE_API_KEY")
        try:
            # Allow GPS coordinates (lat,lon) as direct input
            if ',' in location:
                lat, lon = [x.strip() for x in location.split(',', 1)]
                weather = fetch_weather(lat, lon, api_key)
                forecast = fetch_forecast(lat, lon, api_key)
            else:
                geo = geocode_location(location, api_key)
                lat, lon = geo['lat'], geo['lon']
                weather = fetch_weather(lat, lon, api_key)
                forecast = fetch_forecast(lat, lon, api_key)
            # Only proceed if location resolution succeeds
            if lat and lon:
                # Air Quality
                try:
                    air_quality = get_air_quality(lat, lon, api_key)
                except Exception as aqe:
                    air_quality = {'error': f"Air quality unavailable: {aqe}"}
                # Google Map embed url
                map_url = f"https://www.google.com/maps?q={lat},{lon}&z=10&output=embed"
                # YouTube videos
                try:
                    # Prefer city/country for search if available, fallback to location string
                    search_query = None
                    if weather and weather.get('name'):
                        search_query = weather['name']
                        if weather.get('sys', {}).get('country'):
                            search_query += f" {weather['sys']['country']}"
                    if not search_query:
                        search_query = location
                    youtube_videos = search_youtube_videos(search_query, youtube_api_key)
                except Exception:
                    youtube_videos = []
        except Exception as e:
            error = f"Could not get weather for '{location}': {e}"
    return render_template(
        "index.html",
        weather=weather,
        forecast=forecast,
        location=location,
        error=error,
        air_quality=air_quality,
        youtube_videos=youtube_videos,
        map_url=map_url
    )

@main_bp.route("/records")
def list_records():
    records = WeatherRecord.query.order_by(WeatherRecord.created_at.desc()).all()
    return render_template("list.html", records=records)

@main_bp.route("/records/create", methods=["GET", "POST"])
def create_record():
    if request.method == "POST":
        location_input = request.form.get("location_input", "").strip()
        date_from = request.form.get("date_from", "")
        date_to = request.form.get("date_to", "")

        # Validate inputs
        if not location_input or not date_from or not date_to:
            flash("All fields are required.", "danger")
            return redirect(url_for("main.create_record"))

        try:
            dt_from = datetime.strptime(date_from, "%Y-%m-%d").date()
            dt_to = datetime.strptime(date_to, "%Y-%m-%d").date()
            if dt_from > dt_to:
                flash("Start date must be before end date.", "danger")
                return redirect(url_for("main.create_record"))
        except Exception:
            flash("Invalid date format.", "danger")
            return redirect(url_for("main.create_record"))

        # Fetch weather data and resolve location
        api_key = get_owm_api_key()
        try:
            if ',' in location_input:
                lat, lon = [x.strip() for x in location_input.split(',', 1)]
                geo = {"name": location_input, "country": ""}
            else:
                geo = geocode_location(location_input, api_key)
                lat, lon = geo['lat'], geo['lon']
            resolved_location = f"{geo.get('name', location_input)} ({geo.get('country', '')})"
            weather_data = {
                "current": fetch_weather(lat, lon, api_key),
                "forecast": fetch_forecast(lat, lon, api_key),
            }
        except Exception as e:
            flash(f"Error fetching weather: {e}", "danger")
            return redirect(url_for("main.create_record"))

        record = WeatherRecord(
            location_input=location_input,
            resolved_location=resolved_location,
            date_from=dt_from,
            date_to=dt_to,
            weather_data=json.dumps(weather_data)
        )
        db.session.add(record)
        db.session.commit()
        flash("Weather record created.", "success")
        return redirect(url_for("main.list_records"))

    return render_template("create.html")

@main_bp.route("/records/<int:record_id>/edit", methods=["GET", "POST"])
def edit_record(record_id):
    record = WeatherRecord.query.get_or_404(record_id)
    if request.method == "POST":
        location_input = request.form.get("location_input", "").strip()
        date_from = request.form.get("date_from", "")
        date_to = request.form.get("date_to", "")

        if not location_input or not date_from or not date_to:
            flash("All fields are required.", "danger")
            return redirect(url_for("main.edit_record", record_id=record_id))

        try:
            dt_from = datetime.strptime(date_from, "%Y-%m-%d").date()
            dt_to = datetime.strptime(date_to, "%Y-%m-%d").date()
            if dt_from > dt_to:
                flash("Start date must be before end date.", "danger")
                return redirect(url_for("main.edit_record", record_id=record_id))
        except Exception:
            flash("Invalid date format.", "danger")
            return redirect(url_for("main.edit_record", record_id=record_id))

        api_key = get_owm_api_key()
        try:
            if ',' in location_input:
                lat, lon = [x.strip() for x in location_input.split(',', 1)]
                geo = {"name": location_input, "country": ""}
            else:
                geo = geocode_location(location_input, api_key)
                lat, lon = geo['lat'], geo['lon']
            resolved_location = f"{geo.get('name', location_input)} ({geo.get('country', '')})"
            weather_data = {
                "current": fetch_weather(lat, lon, api_key),
                "forecast": fetch_forecast(lat, lon, api_key),
            }
        except Exception as e:
            flash(f"Error fetching weather: {e}", "danger")
            return redirect(url_for("main.edit_record", record_id=record_id))

        record.location_input = location_input
        record.resolved_location = resolved_location
        record.date_from = dt_from
        record.date_to = dt_to
        record.weather_data = json.dumps(weather_data)
        db.session.commit()
        flash("Weather record updated.", "success")
        return redirect(url_for("main.list_records"))

    return render_template("edit.html", record=record)

@main_bp.route("/records/<int:record_id>/delete", methods=["POST"])
def delete_record(record_id):
    record = WeatherRecord.query.get_or_404(record_id)
    db.session.delete(record)
    db.session.commit()
    flash("Weather record deleted.", "success")
    return redirect(url_for("main.list_records"))

@main_bp.route('/info')
def info():
    return render_template('info.html')

@main_bp.route('/records/<int:record_id>')
def view_record(record_id):
    record = WeatherRecord.query.get_or_404(record_id)
    weather_data = {}
    air_quality = None
    try:
        weather_data = json.loads(record.weather_data)
        # Get lat/lon for air quality
        if "current" in weather_data:
            lat = weather_data["current"].get("coord", {}).get("lat")
            lon = weather_data["current"].get("coord", {}).get("lon")
            if lat and lon:
                api_key = get_owm_api_key()
                air_quality = get_air_quality(lat, lon, api_key)
    except Exception:
        pass

    youtube_videos = []
    api_key = os.environ.get("YOUTUBE_API_KEY") or current_app.config.get("YOUTUBE_API_KEY")
    if api_key:
        try:
            location_query = record.resolved_location.split('(')[0].strip()
            youtube_videos = search_youtube_videos(location_query, api_key)
        except Exception:
            youtube_videos = []
    return render_template(
        'view.html',
        record=record,
        weather_data=weather_data,
        youtube_videos=youtube_videos,
        air_quality=air_quality
    )

def serialize_record(record):
    """Convert a WeatherRecord SQLAlchemy object to a dict for export."""
    data = {
        'id': record.id,
        'location_input': record.location_input,
        'resolved_location': record.resolved_location,
        'date_from': record.date_from.strftime('%Y-%m-%d'),
        'date_to': record.date_to.strftime('%Y-%m-%d'),
        'created_at': record.created_at.strftime('%Y-%m-%d %H:%M'),
        'weather_data': record.weather_data,
    }
    return data

@main_bp.route('/export/json')
def export_json():
    records = WeatherRecord.query.all()
    out = [serialize_record(r) for r in records]
    return Response(json.dumps(out, indent=2), mimetype='application/json',
                    headers={"Content-Disposition": "attachment;filename=weather_records.json"})

@main_bp.route('/export/csv')
def export_csv():
    records = WeatherRecord.query.all()
    output = io.StringIO()
    fieldnames = list(serialize_record(records[0]).keys()) if records else []
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()
    for r in records:
        writer.writerow(serialize_record(r))
    return Response(output.getvalue(), mimetype='text/csv',
                    headers={"Content-Disposition": "attachment;filename=weather_records.csv"})

@main_bp.route('/export/xml')
def export_xml():
    records = WeatherRecord.query.all()
    root = ET.Element('WeatherRecords')
    for rec in records:
        rec_elem = ET.SubElement(root, 'WeatherRecord')
        for k, v in serialize_record(rec).items():
            ET.SubElement(rec_elem, k).text = str(v)
    xml_str = ET.tostring(root, encoding='utf-8')
    return Response(xml_str, mimetype='application/xml',
                    headers={"Content-Disposition": "attachment;filename=weather_records.xml"})

@main_bp.route('/export/markdown')
def export_markdown():
    records = WeatherRecord.query.all()
    md = "# Weather Records Export\n\n"
    for rec in records:
        d = serialize_record(rec)
        md += f"## Record ID: {d['id']}\n"
        md += f"- **Location Input:** {d['location_input']}\n"
        md += f"- **Resolved Location:** {d['resolved_location']}\n"
        md += f"- **Date Range:** {d['date_from']} to {d['date_to']}\n"
        md += f"- **Created At:** {d['created_at']}\n"
        md += f"- **Weather Data:**\n\n```json\n{d['weather_data']}\n```\n\n"
    return Response(md, mimetype='text/markdown',
                    headers={"Content-Disposition": "attachment;filename=weather_records.md"})

@main_bp.route('/export/pdf')
def export_pdf():
    records = WeatherRecord.query.all()
    out = io.BytesIO()
    c = canvas.Canvas(out, pagesize=letter)
    width, height = letter
    y = height - 40
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "Weather Records Export")
    y -= 30
    c.setFont("Helvetica", 10)
    for rec in records:
        d = serialize_record(rec)
        text = f"ID: {d['id']}, Location: {d['resolved_location']}, Date: {d['date_from']} to {d['date_to']}, Created: {d['created_at']}"
        c.drawString(50, y, text)
        y -= 15
        # Add Weather Data (formatted)
        try:
            weather = json.loads(d['weather_data'])
            weather_str = json.dumps(weather, indent=2)
        except Exception:
            weather_str = str(d['weather_data'])
        for line in weather_str.splitlines():
            c.drawString(70, y, line)
            y -= 12
            if y < 50:
                c.showPage()
                y = height - 40
        y -= 10  # Extra space after each record
        if y < 50:
            c.showPage()
            y = height - 40
    c.save()
    out.seek(0)
    return send_file(out, mimetype='application/pdf', as_attachment=True, download_name='weather_records.pdf')

@main_bp.route("/create-db")
def create_db():
    db.create_all()
    return "✅ Database tables created successfully!"

