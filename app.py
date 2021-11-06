from flask import Flask
from books_bp import books

app = Flask(__name__)

app.register_blueprint(books, url_prefix='/books')

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"
 