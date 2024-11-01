# backend/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

from src.config.config import Config

db = SQLAlchemy()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    # Import các blueprint
    from .routes.auth_routes import auth_bp
    from .routes.menu_routes import menu_bp
    # Register routes
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(menu_bp)
    with app.app_context():
        db.create_all()

    return app
