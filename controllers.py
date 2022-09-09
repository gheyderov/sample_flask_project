from flask import render_template, request
from app import app
from forms import ContactForm, ReviewForm
# from model import books, category
from models import Contact, Product, Review


@app.route('/', endpoint='home')
def main():
    products = Product.query.all()
    return render_template('index.html', books=products)


@app.route('/product/<int:pk>', endpoint='product', methods = ['GET', 'POST'])
def products(pk):
    book = Product.query.filter_by(id=pk).first()
    
    form = ReviewForm()
    if request.method == 'POST':
        print(form.data)
        print('post')
        form = ReviewForm(request.form)
        if form.validate_on_submit():
            print('valid')
            review = Review(
                name = form.name.data,
                email = form.email.data,
                message = form.message.data
            )
            review.product_id = pk
            review.save()
    return render_template('book.html', book = book,  pk=pk, form = form)


@app.route('/contact/', endpoint='contact', methods = ['GET', 'POST'])
def contact():
    form = ContactForm()
    print(form.data)
    if request.method == 'POST':
        print(form.data)
        form = ContactForm(request.form)
        if form.validate_on_submit():
            contact = Contact(
                name = form.name.data,
                email = form.email.data,
                company = form.company.data,
                message = form.message.data,
                is_subcribe = form.is_subscribe.data
            )
            contact.save()
    return render_template('contact.html', form = form)