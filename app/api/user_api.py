# app/api/user_api.py

from flask_restful import Resource
from flask import request
from ..models.user import User
from ..extensions import db

class UserListAPI(Resource):
    def get(self):
        users = User.query.all()
        return [{'id': user.id, 'username': user.username, 'email': user.email} for user in users], 200
    
    def post(self):
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        if not username or not email:
            return {'message': 'Username and email are required'}, 400
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'User created', 'id': new_user.id}, 201

class UserAPI(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return {'id': user.id, 'username': user.username, 'email': user.email}, 200
