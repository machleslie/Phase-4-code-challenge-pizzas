from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Resturant(db.Model):
    __tablename__ = 'resturants'
    
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,nullable=False)
    address=db.Column(db.String,nullable=False)
    
    pizzas=db.relationship('resturant_pizza',backref='resturants')
    
class Pizza(db.Model):
    __tablename__='pizzas'
    
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,nullable=False)
    ingredients=db.Column(db.String,nullable=False)
    
    resturant=db.relationship('resturant_pizza',backref='pizzas')
class ResturantPizza(db.Model):
    __tablename__="resturant_pizza"
    
    
    resturant_id=db.Column(db.Integer,db.ForeignKey("resturants.id"),primary_key=True)
    pizza_id=db.Column(db.Integer,db.ForeignKey('pizza.id'),primary_key=True)
    