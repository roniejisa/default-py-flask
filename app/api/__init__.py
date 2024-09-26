# app/api/__init__.py

from flask_restful import Api
from .user_api import UserListAPI, UserAPI

def register_api(app):
    api = Api(app)
    api.init_app(app)  # Khởi tạo API với Flask app
    api.add_resource(UserListAPI, '/api/users')  # Đăng ký resource cho danh sách người dùng
    api.add_resource(UserAPI, '/api/users/<int:user_id>')  # Đăng ký resource cho người dùng cụ thể
