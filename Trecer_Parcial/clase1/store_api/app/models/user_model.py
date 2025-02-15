import json
from app.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin,db.Model):
    __tablename__ = "Usuarios"
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(50),unique=True ,nullable=False)
    password = db.Column(db.String(128),nullable=False)
    roles = db.Column(db.String(50),nullable=False)
    def __init__(self,username,password,roles=["user"]):
        self.username = username
        self.roles = json.dumps(roles)
        self.password = generate_password_hash(password)
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def find_user_by_name(username):
        return User.query.filter_by(username=username).first()