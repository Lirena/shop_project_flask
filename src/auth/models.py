from config import db
from sqlalchemy import Column, Integer, String, Sequence


USER_ID_SEQ = Sequence('user_id_seq')

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer(), USER_ID_SEQ, primary_key=True, server_default=USER_ID_SEQ.next_value())
    login = db.Column(db.String(80), unique=False, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    admin_access = db.Column(db.Boolean(),unique=False, nullable=False, default=False)

    def __init__ (self, login, password, admin_access):
            self.login = login
            self.password = password
            self.admin_access = admin_access

    def __repr__(self):
        return "User(%d, %s, %s, %s)" %(self.id, self.login, self.password, self.admin_access)




'''
CREATE TABLE users(
id serial primary key,
login varchar,
password varchar,
admin_access boolean
);
'''
#create sequence USER_ID_SEQ increment 10 start 10;

'''
INSERT INTO users (login, password, admin_access)
VALUES ('admin', 'adminpassword', 'true'), 
('user_a', 'password1', 'false'), 
('user_b', 'password2', 'false'),
('user_c', 'password3', 'false'),
('user_d', 'password4', 'false');
'''

