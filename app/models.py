from datetime import datetime
from app import db
from random import randint

class Signature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    second_name = db.Column(db.String(45), nullable=False)
    verified = db.Column(db.Boolean(), default=False)
    affiliation = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Podpis {:<4} | {:<20} {:<20} | Email: {}>\n'.format(self.id, self.first_name, self.second_name, self.email)