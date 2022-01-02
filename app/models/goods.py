from app import db
from sqlalchemy.utils.types.choice import ChoiceType
class NotenoughStock(Exception):
    def __str__(self) -> str:
        return "제고는 음수가 될 수 없음"
class Goods(db.Model):
    __tablename__="goods"
    choice=[(u'undergraduate', u'재학생'), (u'graduate', u'졸업생')]
    id=db.Column(db.BigInteger,primary_key=True)
    name=db.Column(db.String(32),unique=True,index=True)
    stock=db.Column(db.Integer)
    doll_type=db.Column(ChoiceType(choice))

    def __init__(self,id,name,stock,doll_type):
        self.id=id
        self.name=name
        self.stock=stock
        self.doll_type=doll_type

    def modif_stock(self,stock_changed):
        if stock_changed>0:
            self.stock+=stock_changed
        else:
            try:
                temp=self.stock+stock_changed
                if temp<0:
                    raise NotenoughStock
                else:
                    self.stock=temp
                    return self.stock
            except NotenoughStock as n:
                return(n)
    