from flask import render_template, request, redirect, session, flash, make_response, g, abort
from flask import Blueprint

from config import app, db

from src.orders.lib.bl import create_order, fetch_orders, fetch_orders_by_user
from src.auth.lib.bl import is_admin

mod_order = Blueprint('order', __name__)

@mod_order.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@mod_order.route("/orders", methods=['GET'])
def proc():
    if g.user and is_admin(session.get('user')):
        return render_template('orders.html', items=fetch_orders())
    elif g.user:
    	return render_template('orders.html', items=fetch_orders_by_user(session.get('user')))
    return redirect ('/login')

@mod_order.route("/cart", methods=['GET'])
def get_cart():
    return render_template('cart.html')