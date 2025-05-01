from functools import wraps
from flask import request, jsonify
import jwt
from .config import JWT_SECRET

def jwt_required_graphql(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        auth = request.headers.get('Authorization', None)
        if not auth or not auth.startswith("Bearer "):
            return jsonify({"error": "Missing or invalid token"}), 401
        try:
            token = auth.split(" ")[1]
            payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
            request.user_id = payload["sub"]
        except Exception:
            return jsonify({"error": "Invalid token"}), 401
        return fn(*args, **kwargs)
    return wrapper
