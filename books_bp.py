from collections import namedtuple
from types import SimpleNamespace
from flask import Blueprint, render_template, request, redirect, url_for
from flask.json import dump
from db import Book

def parse_form():
    f = {**request.form}
    f['yearPublished'] = int(f['yearPublished'])
    return f

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
    book = Book(**parse_form())
    return redirect(url_for('books.show', book_id=book.id))

@books.route('/<book_id>/edit')
def edit(book_id):
    return render_template('books/form.html', book=Book.get(book_id))

@books.route('/<book_id>', methods=["POST"])
def update(book_id):
    book = Book.get(book_id)
    book.set(**parse_form())
    return redirect(url_for('books.show', book_id=book.id))

@books.route('/<book_id>/delete', methods=["POST"])
def delete(book_id):
    Book.delete(book_id)
    return redirect(url_for('books.index'))
