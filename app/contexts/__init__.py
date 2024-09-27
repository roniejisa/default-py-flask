from ..models.user import User
from flask import session

def register_context(app):
    @app.context_processor
    def inject_user():
        user_id = session.get('user_id')
        if user_id:
            user = User.query.get(user_id)
            return {'current_user': user}
        return {'current_user': None}