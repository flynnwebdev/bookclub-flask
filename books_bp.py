from flask import Blueprint, render_template
from db import Book

books = Blueprint('books', __name__)

@books.route('/')
def index():
    return render_template('books/index.html', books=list(Book.select()))

@books.route('/<book_id>')
def show(book_id):
    return render_template('books/show.html', book=Book.get(book_id))

@books.route('/new')
def new():
    return render_template('books/form.html')

@books.route('/', methods=["POST"])
def create():
    return "You POSTed to /books"

@books.route('/<book_id>/edit')
def edit(book_id):
    return render_template('books/form.html', book=Book.get(book_id))

@books.route('/<book_id>', methods=["PUT"])
def update(book_id):
    pass
