
# app/models/__init__.py

from .user import User
from .record import Record
from .comment import Comment
from .media import Media
from .notification import Notification


# # app/__init__.py

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from config import Config

# db = SQLAlchemy()
# migrate = Migrate()

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)
    
#     db.init_app(app)
#     migrate.init_app(app, db)
    
#     with app.app_context():
#         from .models import User, Record, Comment, Media, Notification
#         db.create_all()
    
#     # Register blueprints or routes here
    
#     return app




# # server/models/user.py
# from datetime import datetime
# from werkzeug.security import generate_password_hash, check_password_hash
# from . import db

# class User(db.Model):
#     __tablename__ = 'users'

#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     password_hash = db.Column(db.String(120), nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

#     # Relationships
#     records = db.relationship('Record', backref='user', lazy=True)
#     comments = db.relationship('Comment', backref='user', lazy=True)

#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)

#     def create_user(self):
#         db.session.add(self)
#         db.session.commit()

#     @staticmethod
#     def get_user_by_id(user_id):
#         return User.query.get(user_id)
