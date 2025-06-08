from dotenv import load_dotenv
load_dotenv()

from app import create_app
from app.models import db

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    # Use the PORT environment variable for compatibility with cloud providers
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)