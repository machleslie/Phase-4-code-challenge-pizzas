from flask import Blueprint,request,jsonify
from models import Resturant,db



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
    
@resturant_bp.route('/',methods=["POST"])
def create_resturant():
    """Creates a new resturant and returns it with an id."""
    data=request.json  
    new_resturant=Resturant(name=data['name'],address=data['address'])
    if new_resturant:        
        db.session.add(new_resturant)
        db.session.commit() 
        return jsonify({'message':f"Resturant {data['name']} created succesfully"}),201
    else:
        return jsonify({"messsage":"Error trying to create message"})

@resturant_bp.route("/<int:id>/", methods = ['GET','PUT','DELETE'])
def modify_resturant(id):
    resturant=Resturant.query.filter_by(id=id).first()
    
    if resturant:
        if request.method == "GET":
            # Return a single resturant details
            return jsonify({
                'id':resturant.id,
                'name':resturant.name,
                'address':resturant.address,
                'pizzas':[pizza.serialize for pizza in resturant.pizzas]
                
            })
        elif request.method=='PUT':
            # Update the resturant info
            data=request.json
            resturant.name=data.get('name',resturant.name)
            resturant.address=data.get("address",resturant.address)
            db.session.commit()
            return jsonify({'message':'Resturant updated successfully'}),202
        
        elif request.method == 'DELETE':
            # Delete the resturant
            db.session.delete(resturant)
            db.session.commit()
            return jsonify({'message':'Deleted Successfully'}),200
    else:
        return jsonify({'error':'No such Resturant found!'}),404
