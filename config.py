from flask import Flask, session

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:0492805853@localhost/cake_shop'
app.secret_key = "super secret key"
db = SQLAlchemy(app) 

from src.auth.view import mod_auth
from src.orders.view import mod_order
from src.items.view import mod_item

app.register_blueprint(mod_auth)
app.register_blueprint(mod_order)
app.register_blueprint(mod_item)

from src.auth.models import *
from src.auth.view import *
from src.orders.models import *
from src.orders.view import *
from src.items.models import *
from src.items.view import *

db.create_all()

 