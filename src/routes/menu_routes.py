# routes/menu_routes.py
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

menu_bp = Blueprint('menu', __name__)

@menu_bp.route('/menu', methods=['GET'])
@jwt_required()
def get_menu():
    menu_items = [
        {"id": 1, "label": "Hộ gia đình", "icon": "home-outline", "color": "yellow"},
        {"id": 2, "label": "Tổ chức", "icon": "business-outline", "color": "blue"},
    ]
    return jsonify(menu_items)
