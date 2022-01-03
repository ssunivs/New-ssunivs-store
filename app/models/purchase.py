from app import db
import datetime
status_choice=[(u'processing',u'처리중'),(u'completed',u'완료'),(u'canceled',u'취소'),
(u'delievering',u'배송중')]
#주문 테이블
class purcahse(db.Model):
    __tablename__="purchase"
    id=db.Column(db.String(16),primary_key=True,unique=True)
    customer=db.Column(db.BigInteger,db.ForeignKey('users.id'))
    date_time=db.Column(db.DateTime(timezone=True),default=datetime.datetime.utcnow()+datetime.timedelta(hours=9))
    status=db.Column(ChoiceType(status_choice))
    total_price=db.Column(db.BigInteger)
    #배송관련 정보 추가 필요해보임(다른 테이블로, foreign key)
    #결제관련 정보 추가 
#주문별 구매 상품 및 수량 테이블
class purchase_goods(db.Model):
    __tablename__="purchase_detail"
    id=db.Column(db.BigInteger,primary_key=True)
    purchase_number=db.Column(db.String(16),db.ForeignKey('purchase.id'))
    goods=db.Column(db.String(32),db.ForeignKey('goods.name'))
    count=db.COlumn(db.Integer)
    price=db.Column(db.BigInteger)