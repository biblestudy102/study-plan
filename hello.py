
from flask import Flask, render_template


# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')
def index():
    stuff = "This is a <strong>bold</strong> text."
    fruits = ['apple', 'banana', 'orange', 'stawberry']
    return render_template('index.html', stuff=stuff, fruits=fruits)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# Interal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500
