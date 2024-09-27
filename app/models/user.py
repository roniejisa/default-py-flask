from ..extensions import db
from datetime import datetime
from ..utils import is_valid_email, is_valid_phone
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=True)
    lastname = db.Column(db.String(100), nullable=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<User {self.username}>'
    
    @classmethod
    def getType(cls, username):
        if is_valid_phone(username):
            return 'phone'
        if is_valid_email(username):
            return 'email'
        return 'username'

    @classmethod
    def userExist(cls,username):
        field = cls.getType(username)
        if field == 'email':
            return cls.query.filter_by(email=username).first()
        elif field == 'phone':
            return cls.query.filter_by(phone=username).first()
        else:
            return cls.query.filter_by(username=username).first()
        