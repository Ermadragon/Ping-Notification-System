from . import db
import uuid

class MockActivity(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.String(36), nullable=False)
    activity_type = db.Column(db.String(50))  # 'purchase' or 'browsing'
    product = db.Column(db.String(100))
