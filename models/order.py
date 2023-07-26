from app import db

class Order(db.Model):

    __tablename__ = "List of orders"

    id = db.Column(db.Integer, primary_key=True)
    payment_method = db.Column(db.String(20))
    date = db.Column(db.String(30))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))