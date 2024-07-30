# app/models/media.py

from . import db

class Media(db.Model):
    __tablename__ = 'media'
    
    id = db.Column(db.Integer, primary_key=True)
    file_path = db.Column(db.String(255), nullable=False)
    media_type = db.Column(db.String(20), nullable=False)  # e.g., 'image', 'video'
    record_id = db.Column(db.Integer, db.ForeignKey('records.id'), nullable=False)








# # server/models/media.py
# from datetime import datetime
# from . import db

# class Media(db.Model):
#     __tablename__ = 'media'

#     id = db.Column(db.Integer, primary_key=True)
#     record_id = db.Column(db.Integer, db.ForeignKey('records.id'), nullable=False)
#     file_path = db.Column(db.String(255), nullable=False)
#     media_type = db.Column(db.String(50), nullable=False)  # image or video
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)

#     def create_media(self):
#         db.session.add(self)
#         db.session.commit()

#     def delete_media(self):
#         db.session.delete(self)
#         db.session.commit()

#     @staticmethod
#     def get_media_by_record(record_id):
#         return Media.query.filter_by(record_id=record_id).all()
