from flask import Blueprint, jsonify
from sqlalchemy import text
from app.extensions import db

health_bp = Blueprint("health", __name__)

@health_bp.route("/db")
def db_health():
    try:
        db.session.execute(text("SELECT 1"))
        db.create_all()
        return jsonify({"status": "Database connected"}), 200
    except Exception as e:
        return jsonify({"status": "Database failed", "error": str(e)}), 500
