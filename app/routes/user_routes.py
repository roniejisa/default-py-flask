from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from ..models.user import User
from ..extensions import db
from ..sockets.all_events import publish_event
from ..emails.send_mail import send_welcome_email
from ..utils import create_hash
user_bp = Blueprint('user', __name__, url_prefix='/users')
import sys


@user_bp.route('/')
def list_users():
    users = User.query.all()
    return render_template('users/users.html', users=users)

@user_bp.route('/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        password_confirm = request.form['password_confirm']
        if not username or not email or not password or not password_confirm:
            flash('Vui lòng nhập đầy đủ thông tin', 'error')
            return redirect(url_for('user.create_user'))

        if password != password_confirm:
            flash('Mật khẩu không khớp','error')
            return redirect(url_for('user.create_user'))
        # Cần kiểm tra xem user đã tồn tại chưa sau đó mới insert
        hashed = create_hash(password)
        new_user = User(username=username, email=email, password=hashed)
        db.session.add(new_user)
        db.session.commit()
        # send_welcome_email(email, username)
         # Gọi sự kiện khi tạo người dùng thành công
        publish_event('user_created', {'id': new_user.id, 'username': username, 'email': email})        
        flash('User created and welcome email sent!','success')
        return redirect(url_for('user.list_users'))

        error = session.error
        print(error)
    return render_template('users/create_user.html')