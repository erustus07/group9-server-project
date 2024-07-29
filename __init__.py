# server/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'supersecretkey'

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        # Import models
        from .models.user import User
        from .models.record import Record
        from .models.comment import Comment
        from .models.media import Media
        from .models.notification import Notification

        # Create tables
        db.create_all()

        # Register blueprints
        from .routes.auth import auth_bp
        from .routes.records import records_bp
        from .routes.comments import comments_bp
        from .routes.media import media_bp
        from .routes.notifications import notifications_bp
        
        app.register_blueprint(auth_bp, url_prefix='/auth')
        app.register_blueprint(records_bp, url_prefix='/records')
        app.register_blueprint(comments_bp, url_prefix='/comments')
        app.register_blueprint(media_bp, url_prefix='/media')
        app.register_blueprint(notifications_bp, url_prefix='/notifications')

    return app
