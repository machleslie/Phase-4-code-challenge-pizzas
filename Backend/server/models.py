from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Resturant(db.Model):
    __tablename__ = 'resturants'
    
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,nullable=False)
    address=db.Column(db.String,nullable=False)
    
    pizzas=db.relationship('ResturantPizza',backref='resturants')
    
class Pizza(db.Model):
    __tablename__='pizzas'
    
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,nullable=False)
    ingredients=db.Column(db.String,nullable=False)
    
    resturant=db.relationship('ResturantPizza',backref='pizzas')
class ResturantPizza(db.Model):
    __tablename__="resturant_pizza"
    
    id=db.Column(db.Integer,primary_key=True)
    resturant_id=db.Column(db.Integer,db.ForeignKey("resturants.id"),primary_key=True)
    pizza_id=db.Column(db.Integer,db.ForeignKey('pizzas.id'),primary_key=True)
    