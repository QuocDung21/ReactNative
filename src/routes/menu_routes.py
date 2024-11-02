# routes/menu_routes.py
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

menu_bp = Blueprint('menu', __name__)

@menu_bp.route('/menu', methods=['GET'])
@jwt_required()
def get_menu():
    menu_items = [
        {"id": 1, "label": "Hộ gia đình", "icon": "home-outline", "color": "yellow","href":''},
        {"id": 2, "label": "Tổ chức", "icon": "business-outline", "color": "blue", "href":''},
        {"id": 3, "label": "Tổ chức", "icon": "business-outline", "color": "blue", "href": ''},
        {"id": 4, "label": "Tổ chức", "icon": "business-outline", "color": "blue", "href": ''},
        {"id": 5, "label": "Tổ chức", "icon": "business-outline", "color": "blue", "href": ''},
        {"id": 6, "label": "Tổ chức", "icon": "business-outline", "color": "blue", "href": ''},
        {"id": 7, "label": "Tổ chức", "icon": "business-outline", "color": "blue", "href": ''},
        {"id": 8, "label": "Tổ chức", "icon": "business-outline", "color": "blue", "href": ''},
    ]
    return jsonify(menu_items)
