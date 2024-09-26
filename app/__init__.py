# app/__init__.py

from flask import Flask
from .config import Config
from .extensions import db, migrate, redis_client, mail, socketio
from .routes import register_routes
from .api import register_api  # Đảm bảo bạn đã import
from .events import register_events

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    redis_client.init_app(app)
    mail.init_app(app)
    socketio.init_app(app)

    # Register API endpoints
    register_api(app)  # Khởi tạo API ở đây
    # Register routes
    register_routes(app)

    # In tất cả các route
    with app.app_context():
        print("All registered routes:")
        print(app.url_map)
    # Register event handlers
    register_events(socketio)

    return app