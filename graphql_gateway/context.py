def get_context():
    from flask import request
    return {
        "user_id": getattr(request, "user_id", None),
        "headers": {"Authorization": request.headers.get("Authorization", "")}
    }
