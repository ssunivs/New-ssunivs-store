import sqlalchemy
from app import db
from sqlalchemy.orm.base import MANYTOMANY
class Image(db.Model):
    __tablename__="image"
    id=db.Column(sqlalchemy.types.BigInteger,primary_key=True,autoincrement=True)
    url=db.Column(sqlalchemy.types.String(80))
    image_News=sqlalchemy.orm.relationship("News",MANYTOMANY)