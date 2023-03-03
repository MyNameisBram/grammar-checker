from app.extensions import db
from sqlalchemy.sql import func


class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    text = db.Column(db.String(1000), nullable=False)
