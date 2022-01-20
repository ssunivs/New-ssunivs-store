from sqlalchemy.types import BigInteger
from sqlalchemy.orm.base import ONETOMANY
from app import db, bcrypt
import sqlalchemy
class cart(db.Model):
    __tablename__="cart"
    id=db.Column(BigInteger,priamry_key=True)
    cart_goods_list=sqlalchemy.orm.relationship("cart_goods",ONETOMANY)
    shipping=db.Column(BigInteger)

class cart_goods(db.Model):
    __tablename__="cart_goods"
    id=db.Column(BigInteger,primary_key=True)
    goods=sqlalchemy.orm.relationship("goods")
    count=db.Column(BigInteger)
