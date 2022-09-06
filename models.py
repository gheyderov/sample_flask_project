from extensions import db

class Product(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(200), nullable = True)
    price = db.Column(db.Integer())
    description = db.Column(db.String(200))
    image = db.Column(db.String(255))
    brand = db.Column(db.String(100))
    category_id = db.Column(db.ForeignKey('category.id'))

    def __init__(self, name, price, description, image):
        self.name = name
        self.price = price
        self.description = description
        self.image = image

    def __repr__(self):
        return self.name


class Category(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(200), nullable = True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name