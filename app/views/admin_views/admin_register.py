from flask import request, jsonify
from app.services.admin_services.admin_register_service import admin_register 

def admin_register_view():

    data = request.get_json()

    if not data:
        return jsonify({
            "status": "BAD_REQUEST",
            "message": "Request body must be JSON"
        }), 400

    response = admin_register(data)

    print("response=================", response)

    return jsonify(response), response.get("status_code")
