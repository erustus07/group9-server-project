# server/models/notification.py
from datetime import datetime
from . import db

class Notification(db.Model):
    __tablename__ = 'notifications'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), nullable=False, default='unread')  # unread, read
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def create_notification(self):
        db.session.add(self)
        db.session.commit()

    def mark_as_read(self):
        self.status = 'read'
        db.session.commit()

    @staticmethod
    def get_notifications_by_user(user_id):
        return Notification.query.filter_by(user_id=user_id).all()
