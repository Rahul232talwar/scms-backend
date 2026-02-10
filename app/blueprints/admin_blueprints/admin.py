from flask import Blueprint
from app.views.admin_views.admin_register import admin_register_view



admin_bp = Blueprint("/register", __name__)

@admin_bp.route("/", methods=["POST"])
def admin_register():
    return admin_register_view()