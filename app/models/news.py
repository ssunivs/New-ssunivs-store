from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
import datetime
from sqlalchemy.orm.base import MANYTOMANY
from app import db

class News(db.Model):
    __tablename__= "News"
    id= db.Column(sqlalchemy.types.BigInteger,primary_key=True,unique=True, autoincrement=True)
    written_date=db.Column(sqlalchemy.types.TIMESTAMP(timezone=True))
    title=db.Column(sqlalchemy.types.String(32))
    contents=db.Column(sqlalchemy.types.TEXT(length=None))
    News_image=sqlalchemy.orm.relationship("image",MANYTOMANY)
    def __init__(self,title,contents):
        self.written_date=datetime.datetime.now() 
        self.title=title
        self.contents=contents
