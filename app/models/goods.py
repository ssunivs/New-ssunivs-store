from app import db
from app.exception.NotEnoughQ import NotenoughStockException
from sqlalchemy.utils.types.choice import ChoiceType
from exception import NotenoughStockException
class Goods(db.Model):
    __tablename__="goods"
    choice=[(u'ssuadoll', u'슈아인형'),]
    id=db.Column(db.BigInteger,primary_key=True)
    name=db.Column(db.String(32),unique=True,index=True)
    stock=db.Column(db.Integer)
    goods_type=db.Column(ChoiceType(choice))

    def __init__(self,id,name,stock,doll_type):
        self.id=id
        self.name=name
        self.stock=stock
        self.doll_type=doll_type

    def add_stock(self,amount):
        self.stock+=amount
        return self.stock
    
    def reduce_stock(self,amount):
        if self.stock-amount<0:
            raise NotenoughStockException
        else:
            self.stock-=amount
