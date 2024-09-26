from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models.user import User
from ..extensions import db
from ..emails.send_mail import send_welcome_email
home_bp = Blueprint('home', __name__, url_prefix='/')

@home_bp.route('/')
def home():
    return render_template('index.html')