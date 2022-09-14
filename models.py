from extensions import db, login_manager
from flask_login import UserMixin
from werkzeug.security import check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(200), unique = True)
    email = db.Column(db.String(200), nullable = True)
    password = db.Column(db.String(255), nullable = True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def save(self):
        db.session.add(self)
        db.session.commit()
    


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class Product(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(200), nullable = True)
    price = db.Column(db.Integer())
    description = db.Column(db.String(200))
    image = db.Column(db.String(255))
    brand = db.Column(db.String(100))
    category_id = db.Column(db.ForeignKey('category.id'))

    def __init__(self, name, price, description, image, brand, category_id):
        self.name = name
        self.price = price
        self.description = description
        self.image = image
        self.brand = brand
        self.category_id = category_id

    def __repr__(self):
        return self.name

    def save(self):
        db.session.add(self)
        db.session.commit()


class Category(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(200), nullable = True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def save(self):
        db.session.add(self)
        db.session.commit()


class Contact(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(200), nullable = True)
    email = db.Column(db.String(200), nullable = True)
    company = db.Column(db.String(200), nullable = True)
    message = db.Column(db.String(200), nullable = True)
    is_subscribe = db.Column(db.Boolean())

    def __init__(self, name, email, company, message, is_subcribe):
            self.name = name
            self.email = email
            self.company = company
            self.message = message
            self.is_subscribe = is_subcribe

    def __repr__(self):
        return self.name

    def save(self):
        db.session.add(self)
        db.session.commit()


class Review(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(200), nullable = True)
    email = db.Column(db.String(200), nullable = True)
    message = db.Column(db.String(200), nullable = True)
    product_id = db.Column(db.ForeignKey('product.id'))

    def __init__(self, name, email, message):
            self.name = name
            self.email = email
            self.message = message

    def __repr__(self):
        return self.name

    def save(self):
        db.session.add(self)
        db.session.commit()