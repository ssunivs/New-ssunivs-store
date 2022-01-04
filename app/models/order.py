from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy.orm.base import MANYTOONE, ONETOMANY
from app import db
import datetime
import enum
class status(enum.Enum):
    processing='processing'
    completed='completed'
    canceled='canceled'
    delivering='delivering'

''' status_choice=[(u'processing',u'처리중'),(u'completed',u'완료'),(u'canceled',u'취소'),
(u'delivering',u'배송중')] '''

#주문 테이블
class order(db.Model):
    __tablename__="purchase"
    id=db.Column(db.String(16),primary_key=True,unique=True)
    user=sqlalchemy.orm.relationship("User",back_populates="users_order")
    date_time=db.Column(db.DateTime(timezone=True),default=datetime.datetime.utcnow()+datetime.timedelta(hours=9))
    status=db.Column(Enum(status))
    total_price=db.Column(db.BigInteger)
    order_goods_list=sqlalchemy.orm.relationship("order_details",ONETOMANY)
    adress=db.Column(db.String(64))
    def get_total_price(self):


    #결제관련 정보 추가 
#주문별 구매 상품 및 수량 테이블
class order_goods(db.Model):
    __tablename__="order_detail"
    id=db.Column(db.BigInteger,primary_key=True)#one(order)-to-many(order_detail)
    purchase_number=sqlalchemy.orm.relationship("order",MANYTOONE)
    goods=sqlalchemy.orm.relationship("Goods")
    count=db.Column(db.Integer)
    price=db.Column(db.BigInteger)