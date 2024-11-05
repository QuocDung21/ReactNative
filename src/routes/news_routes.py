# routes/news_routes.py
from flask import Blueprint, jsonify, request, abort
from flask_jwt_extended import jwt_required

from src import db
from src.models.news_item import NewsItem

news_bp = Blueprint('news', __name__)

@news_bp.route('/tintuc', methods=['GET'])
def get_tintuc():
    news_items = NewsItem.query.all()
    return jsonify([item.to_dict() for item in news_items])

@news_bp.route('/tintuc/<int:id>', methods=['GET'])
def get_tintuc_detail(id):
    news_item = NewsItem.query.get(id)
    if news_item is None:
        abort(404, description="Tin tức không tồn tại")
    return jsonify(news_item.to_dict())

@news_bp.route('/tintuc', methods=['POST'])
def add_tintuc():
    if not request.json or not all(k in request.json for k in ("title", "image", "description", "date")):
        abort(400, description="Thiếu dữ liệu yêu cầu")
    new_news = NewsItem(
        title=request.json["title"],
        image=request.json["image"],
        description=request.json["description"],
        date=request.json["date"]
    )
    db.session.add(new_news)
    db.session.commit()
    return jsonify(new_news.to_dict()), 201


# 