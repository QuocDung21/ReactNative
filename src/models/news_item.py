# models/news_item.py
from src import db


class NewsItem(db.Model):
    __tablename__ = 'news_items'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.String(10), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "image": self.image,
            "description": self.description,
            "date": self.date
        }
