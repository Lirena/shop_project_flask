from flask import render_template, request, redirect, session, flash, make_response, g, abort
from flask import Blueprint

from config import app, db
from src.items.lib.bl import fetch_list
from src.auth.lib.bl import is_admin

mod_item = Blueprint('item', __name__)

@mod_item.route("/cakes", methods=['GET'])
def proc():
    return render_template('cakes.html', items=fetch_list())

@mod_item.route("/contact",methods=['GET'])
def contact():
	return render_template('contacts.html')

@mod_item.route("/error", methods=['GET'])
def err():
    return render_template('error.html')

@mod_item.route("/", methods=['GET'])
def main():
    return render_template('index.html', items=fetch_list())