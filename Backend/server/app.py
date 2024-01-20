from flask import Flask
from flask_migrate import Migrate
from models import db
from views.resturant_views import resturant_bp


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


Migrate(app, db)
db.init_app(app)

if "__main__" == __name__:
    
    app.register_blueprint(resturant_bp,url_prefix='/resturant')
    app.run(debug=True,port=5555)
