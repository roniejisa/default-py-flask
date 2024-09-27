from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from ..models.user import User
from ..extensions import db
from ..emails.send_mail import send_welcome_email
home_bp = Blueprint('home', __name__, url_prefix='/')


# @home_bp.context_processor
# def inject_user():
#     user_id = session.get('user_id')
#     if user_id:
#         user = User.query.get(user_id)
#         return {'current_user': user}
#     return {'current_user': None}

@home_bp.route('/')
def home():
    return render_template('pages/home.html')