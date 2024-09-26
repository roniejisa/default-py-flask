from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models.user import User
from ..extensions import db
from ..emails.send_mail import send_welcome_email
user_bp = Blueprint('user', __name__, url_prefix='/users')

@user_bp.route('/')
def list_users():
    users = User.query.all()
    return render_template('users.html', users=users)

@user_bp.route('/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        send_welcome_email(email, username)
        flash('User created and welcome email sent!')
        return redirect(url_for('user.list_users'))
    return render_template('create_user.html')