from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_redis import FlaskRedis
from flask_mail import Mail
from flask_restful import Api
from flask_socketio import SocketIO
db = SQLAlchemy()
migrate = Migrate()
redis_client = FlaskRedis()
mail = Mail()
api = Api()
socketio = SocketIO()