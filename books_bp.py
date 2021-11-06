from flask import Blueprint, render_template

books = Blueprint('books', __name__)

@books.route('/')
def index():
    return render_template('books/index.html')
