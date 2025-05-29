from flask import Flask
from app.extensions import db, migrate
from config import config

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()
        
    return app      