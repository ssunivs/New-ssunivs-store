from app import db, bcrypt
import sqlalchemy.orm as orm
from sqlalchemy.orm.base import MANYTOMANY
import sqlalchemy

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.BigInteger, primary_key=True)
    name=db.Column(db.String(6))
    email = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128))
    order_list=db.orm.relationship("order",back_populates="order_user")
    user_cart=orm.relationship("cart")
    user_coupon=orm.relationship("coupon",MANYTOMANY)
    user_address=orm.relationship("address")
    phone=db.Column(db.String(16))

    def __init__(self, email, password):
        self.email = email
        self.password = User.hashed_password(password)

    @staticmethod
    def hashed_password(password):
        return bcrypt.generate_password_hash(password).decode("utf-8")

    @staticmethod
    def get_user_with_email_and_password(email, password):
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return None
