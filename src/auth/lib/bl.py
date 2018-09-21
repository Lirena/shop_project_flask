from src.auth.models import User

from security import hash_password, check_password

from config import db

def fetch_user(_login):
	user = User.query.filter_by(login=_login).first()
	return user

def is_user(_login):
	is_user = fetch_user(_login)
	return is_user

def is_password_valid(_login, user_password):
	hashed_password = fetch_user(_login).password
	return check_password(hashed_password, user_password)

def is_admin(_login):
	return fetch_user(_login).admin_access == True

'''
db.session.add_all([User('admin', hash_password('adminpassword'), True),
            User('user_a', hash_password('password1'), False),
            User('user_b', hash_password('password2'), False),
            User('user_c', hash_password('password3'), False),
            User('user_d', hash_password('password4'), False)])
db.session.commit()
'''
'''    
db.session.add_all([User('admin', hash_password('123'), True),
            User('user', hash_password('345'), False)])
db.session.commit()
'''