from .user_routes import user_bp
from .home_routes import home_bp
from .login_routes import login_bp
from .fallback_routes import fallback_bp

def register_routes(app):
    app.register_blueprint(user_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(fallback_bp)