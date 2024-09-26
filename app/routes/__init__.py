from .user_routes import user_bp
from .home_routes import home_bp
def register_routes(app):
    app.register_blueprint(user_bp)
    app.register_blueprint(home_bp)
