from flask import Blueprint, request, jsonify, current_app
from .models import MockActivity, db
from .utils import get_mock_recommendations, send_kafka_notification

recommend_bp = Blueprint('recommendation', __name__, url_prefix='/recommendations')

@recommend_bp.route('/generate/<user_id>', methods=['POST'])
def generate_recommendation(user_id):
    history = MockActivity.query.filter_by(user_id=user_id).all()
    if not history:
        return jsonify({'msg': 'No activity found'}), 404

    recommendations = get_mock_recommendations(user_id, history)

    # send to Kafka
    for rec in recommendations:
        send_kafka_notification(user_id, rec, current_app.config)

    return jsonify({'msg': 'Recommendations sent', 'recommendations': recommendations})
