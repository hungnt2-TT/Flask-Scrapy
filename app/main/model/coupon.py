from datetime import datetime

from app.main import db


class Coupon(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "coupon"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    coupon_code = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=datetime.now())

    def __repr__(self):
        return f'<Coupon {self.coupon_code} in Url {self.url}>'

