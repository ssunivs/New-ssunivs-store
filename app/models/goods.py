from app import db
from sqlalchemy.utils.types.choice import ChoiceType
class Goods(db.Model):
    __tablename__="goods"
    choice=[(u'undergraduate', u'재학생'), (u'graduate', u'졸업생')]
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(32),unique=True,index=True)
    stock=db.Column(db.Integer)
    doll_type=db.Column(ChoiceType(choice))

    def __init__(self,id,name,stock,doll_type):
        self.id=id
        self.name=name
        self.stock=stock
        self.doll_type=doll_type

    def modif_stock(self,now_stock):
        self.stock=now_stock
        return self.stock
    