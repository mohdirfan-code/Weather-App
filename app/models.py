from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class WeatherRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location_input = db.Column(db.String(128), nullable=False)
    resolved_location = db.Column(db.String(128), nullable=False)
    date_from = db.Column(db.Date, nullable=False)
    date_to = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    weather_data = db.Column(db.Text, nullable=False)  # Store API JSON as text

    def __repr__(self):
        return f"<WeatherRecord {self.resolved_location} {self.date_from} to {self.date_to}>"