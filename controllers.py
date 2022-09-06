from flask import render_template
from app import app
# from model import books, category
from models import Product


@app.route('/', endpoint='home')
def main():
    products = Product.query.all()
    return render_template('index.html', books=products)


@app.route('/product/<int:pk>', endpoint='product')
def products(pk):
    book = Product.query.filter_by(id=pk).first()
    return render_template('book.html', book = book,  pk=pk)