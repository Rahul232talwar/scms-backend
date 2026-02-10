from flask import request, jsonify
from app.services.admin_services.admin_register_service import admin_register 

def admin_register_view():
    data = request.get_json()

    new_admin = admin_register(data)
    print("this is from the view", new_admin)
    return jsonify(new_admin), 201
