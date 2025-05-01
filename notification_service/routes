from flask import Blueprint, jsonify, request
from .models import Notification, db

notification_bp = Blueprint('notification', __name__, url_prefix='/notifications')

@notification_bp.route('/<user_id>/unread', methods=['GET'])
def get_unread(user_id):
    notifications = Notification.query.filter_by(user_id=user_id, read=False).all()
    return jsonify([{
        'id': n.id,
        'type': n.type,
        'content': n.content,
        'sent_at': n.sent_at.isoformat()
    } for n in notifications])

@notification_bp.route('/<notification_id>/read', methods=['POST'])
def mark_as_read(notification_id):
    notification = Notification.query.get_or_404(notification_id)
    notification.read = True
    db.session.commit()
    return jsonify({'msg': 'Marked as read'})
