from config import db
from sqlalchemy import Column, Integer, String, Sequence, Date


ORDER_ID_SEQ = Sequence('order_id_seq')

class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer(), ORDER_ID_SEQ, primary_key=True, server_default=ORDER_ID_SEQ.next_value())
    user_id = db.Column(db.Integer(), unique=False, nullable=False)
    item_id = db.Column(db.Integer(), unique=False, nullable=False)
    number_of_items = db.Column(db.Integer(), unique=False, nullable=False)
    date = db.Column(db.Date(), unique=False, nullable=False)
    status = db.Column(db.String(), unique=False, nullable=False, default='new')


    def __init__ (self, user_id, item_id, number_of_items, date, status):
            self.user_id = user_id
            self.item_id = item_id
            self.number_of_items = number_of_items
            self.date = date
            self.status = status

       
    def __repr__(self):
        return "Order(%s, %s, %d, %d, %s)" %(self.user_id, self.item_id, self.number_of_items, self.date, self.status)


#create sequence ORDER_ID_SEQ increment 10 start 10;

'''
CREATE TYPE status AS ENUM ('done', 'processing', 'new');
CREATE TABLE orders(
id serial,
user_id integer references users(id),
item_id integer references cakes(id),
number_of_items integer,
date date,
status status
);
'''
'''
INSERT INTO orders (user_id, item_id, number_of_items, date, status)
VALUES ('180', '12', '2', '2018-06-15', 'done'),
('180', '8', '1', '2018-06-16', 'done'),
('190', '6', '1', '2018-06-17', 'done'),
('210', '7', '2', '2018-06-19', 'done'),
('180', '11', '3', '2018-06-23', 'processing'),
('200', '13', '1', '2018-06-25', 'new');
'''