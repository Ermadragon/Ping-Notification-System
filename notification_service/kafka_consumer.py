from kafka import KafkaConsumer
import threading, json
from .models import Notification, db
from flask import current_app

def handle_notification(message):
    data = json.loads(message.value.decode('utf-8'))
    notification = Notification(
        user_id=data['user_id'],
        type=data['type'],
        content=data['content']
    )
    db.session.add(notification)
    db.session.commit()

def start_kafka_consumer(app):
    def run():
        with app.app_context():
            consumer = KafkaConsumer(
                app.config['KAFKA_TOPIC'],
                bootstrap_servers=app.config['KAFKA_BOOTSTRAP_SERVERS'],
                auto_offset_reset='earliest',
                group_id='notification-group'
            )
            for message in consumer:
                handle_notification(message)
    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()
