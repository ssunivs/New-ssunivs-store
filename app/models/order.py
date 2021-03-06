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
    order_user=sqlalchemy.orm.relationship("User",back_populates="order_list")
    date_time=db.Column(db.DateTime(timezone=True),default=datetime.datetime.utcnow()+datetime.timedelta(hours=9))
    status=db.Column(Enum(status))
    total_price=db.Column(db.BigInteger)
    order_goods_list=sqlalchemy.orm.relationship("order_goods_list",ONETOMANY)
    adress=db.Column(db.String(64))#composite value?
    shipping=db.Column(sqlalchemy.types.BigInteger)
    memo=db.Column(db.Text(64))
    visit_datetime=db.Column(sqlalchemy.types.DATETIME(timezone=True))
    def get_total_price(self):
        this_order_goods=self.order_goods_list
        totalprice=0
        for good in this_order_goods:
            totalprice+=(good.price*good.count)
        return totalprice

    #결제관련 정보 추가 
#주문별 구매 상품 및 수량 테이블
class order_goods(db.Model):
    __tablename__="order_detail"
    id=db.Column(db.BigInteger,primary_key=True)#one(order)-to-many(order_detail)
    order_id=sqlalchemy.orm.relationship("order",MANYTOONE)
    goods=sqlalchemy.orm.relationship("Goods")
    count=db.Column(db.Integer)
    price=db.Column(db.BigInteger)