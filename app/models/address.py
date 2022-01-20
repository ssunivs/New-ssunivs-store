from app import db

class address(db.Model):
    __tablename__="address"
    id=db.Column(db.BigInteger,primary_key=True)
    province=db.Column(db.String(32))
    city=db.Column(db.String(32))
    district=db.Column(db.String(32))
    detailed=db.Column(db.String(64))
    zipcode=db.Column(db.String(6))