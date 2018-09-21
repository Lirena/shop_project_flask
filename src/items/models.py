from config import db
from sqlalchemy import Column, Integer, String, Sequence


CAKE_ID_SEQ = Sequence('cake_id_seq')

class Cake(db.Model):
    __tablename__ = "cakes"
    id = db.Column(db.Integer(), CAKE_ID_SEQ, primary_key=True, server_default=CAKE_ID_SEQ.next_value())
    name = db.Column(db.String(80), unique=False, nullable=False)
    price = db.Column(db.String(), unique=False, nullable=False)
    text = db.Column(db.String(), unique=False, nullable=False)
    category = db.Column(db.String(80), unique=False, nullable=False)
    img_path = db.Column(db.String(), unique=False, nullable=False)

    def __init__ (self, name, price, text, category):
            self.name = name
            self.price = price
            self.text = text
            self.category = category
            self.img_path = img_path

    def __repr__(self):
        return "Cake(%s, %s, %s, %s)" %(self.name, self.price, self.text, self.category, self.img_path)


'''
create sequence CAKE_ID_SEQ increment 10 start 10;

CREATE TYPE category AS ENUM ('cakes', 'cookies', 'pies');
CREATE TABLE cakes(
id serial primary key,
name varchar,
price varchar,
text varchar,
category category,
img_path varchar
);

INSERT INTO cakes (name, price, text, category, img_path)
VALUES ('Banana Cake', '150', 'some text', 'cakes', '../static/images/items/cakes/banana.jpg'),
('Cheesecake','120', 'some text', 'cakes', '../static/images/items/cakes/cheesecake.jpg'),
('Cupcake','30', 'some text', 'cakes', '../static/images/items/cakes/cupcake.jpg'),
('Fruit Cake','140', 'some text', 'cakes', '../static/images/items/cakes/fruit.jpg'),
('Lemon Tart','125', 'some text', 'cakes', '../static/images/items/cakes/tart.jpg'),
('Macaron','50', 'some text', 'cookies', '../static/images/items/cookies/macaron.jpg'),
('Chocolate Chip Cookie','55', 'some text', 'cookies', '../static/images/items/cookies/chocolatechip.jpg'),
('Outmeal Cookies','45', 'some text', 'cookies', '../static/images/items/cookies/outmeal.jpg'),
('Brownie','100', 'some text', 'pies', '../static/images/items/pies/brownie.jpg'),
('Cherry','110', 'some text', 'pies', '../static/images/items/pies/cherry.jpg'),
('Apple Pie','90', 'some text', 'pies', '../static/images/items/pies/apple.jpg')
;
'''