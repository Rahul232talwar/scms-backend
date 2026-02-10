from functools import wraps
from flask import request, jsonify

def auth_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return jsonify({"error": "Unauthorized"}), 401

        # Attach user like req.user
        request.user = {"id": 1, "role": "admin"}

        return view(*args, **kwargs)

    return wrapped
