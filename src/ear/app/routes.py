from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import BookForm
from app.models import Book

@app.route('/')
@app.route('/index')
def index():
    books = Book.query.all()
    return render_template('index.html', title = 'Home Page', books=books)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        book = Book(
            author=form.author.data,
            title=form.title.data,
            status=form.status.data
        )
        db.session.add(book)
        db.session.commit()
        flash('Your changes have been saved')
        return redirect(url_for('index'))
    return render_template('add_book.html', title='Add Book', form=form)