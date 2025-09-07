from app import db 

class post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer , primary_key = True)
    title = db.Column(db.String(50))
    discription = db.Column(db.String(100))
    username = db.Column(db.String(50))   # new field for author
