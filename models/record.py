# app/models/record.py

from . import db

class Record(db.Model):
    __tablename__ = 'records'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    record_type = db.Column(db.String(50), nullable=False)  # e.g., 'red-flag' or 'intervention'
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    status = db.Column(db.String(50), nullable=False, default='draft')  # e.g., 'under investigation', 'resolved'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    comments = db.relationship('Comment', backref='record', lazy=True)
    media = db.relationship('Media', backref='record', lazy=True)







# # server/models/record.py
# from datetime import datetime
# from . import db

# class Record(db.Model):
#     __tablename__ = 'records'

#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#     type = db.Column(db.String(50), nullable=False)  # red-flag or intervention
#     title = db.Column(db.String(120), nullable=False)
#     description = db.Column(db.Text, nullable=False)
#     latitude = db.Column(db.Float, nullable=True)
#     longitude = db.Column(db.Float, nullable=True)
#     status = db.Column(db.String(50), nullable=False, default='draft')  # draft, under investigation, rejected, resolved
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

#     # Relationships
#     comments = db.relationship('Comment', backref='record', lazy=True)
#     media = db.relationship('Media', backref='record', lazy=True)

#     def create_record(self):
#         db.session.add(self)
#         db.session.commit()

#     def update_record(self, data):
#         for key, value in data.items():
#             setattr(self, key, value)
#         db.session.commit()

#     def delete_record(self):
#         db.session.delete(self)
#         db.session.commit()

#     @staticmethod
#     def get_record_by_id(record_id):
#         return Record.query.get(record_id)

#     @staticmethod
#     def get_records_by_user(user_id):
#         return Record.query.filter_by(user_id=user_id).all()
