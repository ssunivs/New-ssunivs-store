from app import db
from sqlalchemy.utils.types.choice import ChoiceType
from exception.NotEnoughQ import NotenoughStock
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

    def add_stock(self,amount):
        self.stock+=amount
        return self.stock
    
    def reduce_stock(self,amount):
        try:
            if self.stock-amount<0:
                raise NotenoughStock
            else:
                self.stock-=amount
        except NotenoughStock as e:
            print(e)
            return(e)