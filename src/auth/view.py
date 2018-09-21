from flask import render_template, request, redirect, session, flash, make_response, g, abort
from flask import Blueprint

from config import app, db

from src.auth.lib.bl import is_user, is_password_valid
from src.items.lib.bl import fetch_list

mod_auth = Blueprint('auth', __name__)

@mod_auth.route('/login', methods=['GET'])
def home():
    if not session.get('user'):
        return render_template('login.html')
    else:
        return redirect('/orders', code=302)
 
@mod_auth.route('/login', methods=['POST'])
def login_user():
    user = request.form['input_login']
    password = request.form['input_password']
    if is_user(user) and is_password_valid(user, password):
        response = app.make_response(redirect('/list'))  
        response.set_cookie('user',value='user')
        session['user'] = user
    return home()

@mod_auth.route('/logout')
def logout():
   session.pop('user', None)
   return redirect('/')