import json
from kafka import KafkaProducer

def get_mock_recommendations(user_id, history):
    products = list({h.product for h in history})
    recommended = [f"Recommended item based on {p}" for p in products]
    return recommended

def send_kafka_notification(user_id, content, kafka_config):
    producer = KafkaProducer(bootstrap_servers=kafka_config['KAFKA_BOOTSTRAP_SERVERS'])
    message = {
        'user_id': user_id,
        'type': 'recommendation',
        'content': {
            'title': 'Personalized Recommendation',
            'message': content
        }
    }
    producer.send(kafka_config['KAFKA_TOPIC'], json.dumps(message).encode('utf-8'))
    producer.flush()
