from flask import Flask
from app.extensions import db, migrate

from config import config

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)
    
    
    # Register blueprints
    # blueprints imports
    from app.main.views import main_bp
    from app.api.routes import api_bp
    with app.app_context():
        db.create_all()

    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)

    return app

    return app      