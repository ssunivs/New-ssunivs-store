from app import db
from sqlalchemy.orm import relationship
import sqlalchemy

class coupon(db.Model):
    id=db.Column(db.BigInteger,primary_key=True)
    name=db.Column(db.Text(40))
    discount=db.Column(db.BigInteger)
    code=db.Column(db.Text(64))
    issuedate=db.Column(sqlalchemy.types.Date)
    issue_amount=db.Column(db.BigInteger)
    used_amount=db.Column(db.BigInteger)
    