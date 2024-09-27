# app/routes/login_routes.py

from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from ..models.user import User
from ..extensions import db
from ..utils import check_hash
from urllib.parse import urlparse, urljoin

login_bp = Blueprint('login', __name__, url_prefix='/')

@login_bp.route('/dang-nhap', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if not request.form['username'] or not request.form['password']:
            flash('Thiếu thông tin','error')
            return redirect(url_for('login.login'))
        # Kiểm tra user
        user = User.userExist(request.form['username'])
        if not check_hash(request.form['password'], user.password):
            flash('Mật khẩu không chính xác','error')
            return redirect(url_for('login.login'))
        session['user_id'] = user.id
        return redirect(url_for('home.home'))
    return render_template('themes/one/auth/login.html')

@login_bp.route('/dang-xuat')
def logout():
    flash('Bạn đã đăng xuất.', 'info')
    return redirect(url_for('home.home'))