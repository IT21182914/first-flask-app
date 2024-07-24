from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)

from routes.note_routes import note_bp
app.register_blueprint(note_bp)

with app.app_context():
    db.create_all()  # Create tables

if __name__ == '__main__':
    app.run(debug=True)
