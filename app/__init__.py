import os
import re
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .models import db

def subscript_formula(s):
    """
    Replace digits in a chemical formula with unicode subscripts.
    Example: "CO2" -> "CO₂", "PM2_5" -> "PM₂.₅"
    """
    # Handle common particle notation (e.g., PM2_5 to PM₂.₅)
    s = s.replace("_", ".")
    # Replace all digits with subscript unicode
    return re.sub(r'(\d)', lambda m: chr(0x2080 + int(m.group(0))), s)

def create_app(test_config=None):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
    app = Flask(__name__, instance_relative_config=True, template_folder=TEMPLATE_DIR)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY", "dev"),
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{os.path.join(app.instance_path, 'weather_app.db')}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if test_config:
        app.config.update(test_config)

    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError:
        pass

    db.init_app(app)

    # Register jinja filter for chemical subscripts
    app.jinja_env.filters['subscript'] = subscript_formula

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app