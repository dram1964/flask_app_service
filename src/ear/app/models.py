from datetime import datetime
from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), index=True, unique=True)
    author = db.Column(db.String(120), index=True)
    status = db.Column(db.String(30))

    def __repr__(self):
        return '{} by {}'.format(self.title, self.author)
