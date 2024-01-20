from flask import Blueprint
from models import Resturant


resturant_bp=Blueprint('resturant',__name__)

@resturant_bp.route('/')
def get_resturants():
    """Returns a list of all the resturants"""
    resturants=Resturant.query.all()
    
    if resturants:        
        for resturant in resturants:
            return[{
                'id':resturant.id,
                'name':resturant.name,
                'address':resturant.address,
                'pizzas':resturant.pizzas
                
            }]
    else:
        return {'message':'No data found'}