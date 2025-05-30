from flask import Flask
from flask_security import SQLAlchemyUserDatastore
from app.extensions import db, migrate, mail, security


from config import config

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    # Register blueprints
    # blueprints imports
    from app.main.views import main_bp
    from app.api.routes import api_bp
    from app.auth.routes import auth_bp
    

# Register the blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(auth_bp)

# Import models and Initialize Flask-Security
    from app.models.user import User, Role
    from flask_security import hash_password
    import uuid
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, user_datastore)

    with app.app_context():
        db.create_all()

        roles_data = [
            {"name": "super_admin", "description": "Administrator role with full access"},
            {"name": "staff", "description": "Staff role with limited access"},
            {"name": "citizen", "description": "Regular citizen role with basic access"},
            {"name": "guest", "description": "Guest role with minimal access"},
        ]
        for role_data in roles_data:
            role = Role.query.filter_by(name=role_data["name"]).first()
            if not role:
                role = Role(**role_data)
                db.session.add(role)
            
            admin_role = Role.query.filter_by(name="super_admin").first()
            admin_user = User.query.filter_by(email='enock@gmail.com').first()

            if not admin_user:
                admin_user = User(email='enock@gmail.com',
                                  password=hash_password('12345678'),
                                  active=True,
                                  roles=[admin_role],
                                 
                                  )
            db.session.add(admin_user)
            print("database initialized and admin user created successfully")

    return app
