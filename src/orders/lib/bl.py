from src.orders.models import Order
from src.auth.models import User

from config import db



def create_order(_phone_number,_address):    
    db.session.add(Order(_phone_number,_address))
    db.session.commit()
    return create_order

def fetch_orders():
	return Order.query.all()

def fetch_orders_by_user(user):
	_user = User.query.filter_by(login = user).first()
	user_id = _user.id
	return Order.query.filter_by(user_id = user_id)