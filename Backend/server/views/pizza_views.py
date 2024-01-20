from flask import Blueprint,jsonify,request
from models import Pizza,db


pizza_bp=Blueprint('pizza',__name__)

@pizza_bp.route('/')
def get_pizza():
    pizzas=Pizza.query.all()
    
    if pizzas:
        for pizza in pizzas:
            return[{
                'id':pizza.id,
                'name':pizza.name,
                'ingredients':pizza.ingredients
            }]
    else:
        return jsonify({'Error': 'Could not find any pizzas 😆'})
    
    
@pizza_bp.route("/",methods=["POST"])
def create_pizzas():
    
    data=request.json
    
    new_pizza=Pizza(name=data['name'],ingredients=data['ingredients'])
    
    if new_pizza:
        db.session.add(new_pizza)
        db.session.commit()
        return jsonify({"message":"Successfully created a new pizza 😉!"}),201
    
    else:
        return jsonify({"error": "Failed to create the pizza 😞"})
    
    
@pizza_bp.route('/<int:id>/',methods=["GET",'PUT','DELETE'])
def modify_pizza(id):
    pizza = Pizza.query.filter_by(id=id).first()
    
    if pizza:
        if request.method == "PUT":
            data=request.json
            #update name and ingredients fields only
            pizza.name=data.get("name",pizza.name)
            pizza.ingredients=data.get('ingredients',pizza.ingredients)
            db.session.commit()
            return jsonify({'Message':"Pizza updated succesfully 😄"})
        
        elif request.method == "GET":
            return jsonify({
                'id':pizza.id,
                'name':pizza.name,
                'ingredients':pizza.ingredients
                })
            
            
        elif request.method == 'DELETE':
            db.session.delete(pizza)
            db.session.commit()
            return jsonify({'Message':'This pizza has been deleted 🍕'})
            
    else:
        return jsonify({'Error':'The requested pizza does not exist 🍕'})