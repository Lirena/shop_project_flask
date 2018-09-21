from src.items.models import Cake

from config import db


def fetch_list():
	return Cake.query.all()

