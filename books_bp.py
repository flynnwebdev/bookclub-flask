from flask import Blueprint, render_template
from db import cur

books = Blueprint('books', __name__)

@books.route('/')
def index():
    global cur
    cur.execute("SELECT * FROM books ORDER BY title ASC")
    # return json.dumps(cur.fetchall(), default=str)
    return render_template('books/index.html', books=cur.fetchall())

@books.route('/<book_id>')
def show(book_id):
    global cur
    cur.execute("SELECT * FROM books WHERE id=%s", [book_id])
    # return json.dumps(cur.fetchall(), default=str)
    return render_template('books/show.html', book=cur.fetchone())

@books.route('/new')
def new():
    return render_template('books/form.html',
    
    )