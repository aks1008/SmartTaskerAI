from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    balance = db.Column(db.Float, default=0.0)

class ShoppingList(db.Model):
    __tablename__ = 'shoppinglist'
    id = db.Column(db.Integer, primary_key=True)
    itemname = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(100), nullable=False)

class ShoppingListUser(db.Model):
    __tablename__ = 'shoppinglist_user'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('shoppinglist.id'), nullable=False)
    purchased_date = db.Column(db.String(100), nullable=False)  # Use appropriate date type if needed
    quantity = db.Column(db.Integer, nullable=False)
    purchase_mode = db.Column(db.String(20), nullable=False)  # 'inperson' or 'online'
    
    user = db.relationship('User', backref=db.backref('shoppinglist_users', lazy=True))
    item = db.relationship('ShoppingList', backref=db.backref('shoppinglist_users', lazy=True))