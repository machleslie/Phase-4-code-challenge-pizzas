from flask import Blueprint,request,jsonify
from .__init__ import db,ResturantPizza

resturantpizza_bp=Blueprint("resturantpizza", __name__)


@resturantpizza_bp.route('/')
def get_pizza():
    resturantpizzas=ResturantPizza.query.all()
    
    if resturantpizzas:
        for resturantpizza in resturantpizzas:
            return[{
                'id':resturantpizza.id,
                'pizza_id':resturantpizza.pizza_id,
                'resturant_id':resturantpizza.resturant_id
            }]
    else:
        return jsonify({'Error': 'Could not find any resturantpizzas 😆'})
    
    
@resturantpizza_bp.route("/",methods=["POST"])
def create_pizzas():
    
    data=request.json
    
    new_pizza=ResturantPizza(resturant_id=data['resturant_id'],pizza_id=data['pizza_id'],price=data['price'])
    
    if new_pizza:
        db.session.add(new_pizza)
        db.session.commit()
        return jsonify({"message":"Successfully created a new resturantpizza 😉!"}),201
    
    else:
        return jsonify({"error": "Failed to create the resturantpizza 😞"})
    
    
@resturantpizza_bp.route('/<int:id>/',methods=["GET",'PUT','DELETE'])
def modify_resturantpizza(id):
    resturantpizza = ResturantPizza.query.filter_by(id=id).first()
    
    if resturantpizza:
        if request.method == "PUT":
            data=request.json
            
            
            resturantpizza.pizza_id=data.get("pizza_id",resturantpizza.pizza_id)
            resturantpizza.resturant_id=data.get('resturant_id',resturantpizza.resturant_id)
            resturantpizza.price=data.get('price',resturantpizza.price)

            db.session.commit()
            return jsonify({'Message':"resturantpizza updated succesfully 😄"})
        
        elif request.method == "GET":
            return jsonify({
                'price':resturantpizza.price,
                'pizza_id':resturantpizza.pizza_id,
                'resturant_id':resturantpizza.resturant_id
                })
            
            
        elif request.method == 'DELETE':
            db.session.delete(resturantpizza)
            db.session.commit()
            return jsonify({'Message':'This resturantpizza has been deleted 🍕'})
            
    else:
        return jsonify({'Error':'The requested resturantpizza does not exist 🍕'})
