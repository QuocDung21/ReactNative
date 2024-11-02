# backend/__init__.py
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, get_jwt, create_access_token, set_access_cookies, get_jwt_identity
from datetime import timedelta
from src.config.config import Config

db = SQLAlchemy()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    # app.config["JWT_COOKIE_SECURE"] = False
    # app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
    # app.config["JWT_SECRET_KEY"] = "super-secret"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=30)

    # # Using an `after_request` callback, we refresh any token that is within 30
    # # minutes of expiring. Change the timedeltas to match the needs of your application.
    # @app.after_request
    # def refresh_expiring_jwts(response):
    #     try:
    #         exp_timestamp = get_jwt()["exp"]
    #         now = datetime.now(timezone.utc)
    #         target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
    #         if target_timestamp > exp_timestamp:
    #             access_token = create_access_token(identity=get_jwt_identity())
    #             set_access_cookies(response, access_token)
    #         return response
    #     except (RuntimeError, KeyError):
    #         # Case where there is not a valid JWT. Just return the original response
    #         return response

    # Import các blueprint
    from .routes.auth_routes import auth_bp
    from .routes.menu_routes import menu_bp
    from .routes.news_routes import news_bp
    # Register routes
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(menu_bp, url_prefix='/api')
    app.register_blueprint(news_bp, url_prefix='/api')
    with app.app_context():
        db.create_all()

    return app
