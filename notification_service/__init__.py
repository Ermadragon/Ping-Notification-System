from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from .kafka_consumer import start_kafka_consumer

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from .routes import notification_bp
    app.register_blueprint(notification_bp)

    with app.app_context():
        db.create_all()
        start_kafka_consumer(app)

    return app
