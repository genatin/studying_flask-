from app import app
from .generating_view import generate_view
from flask import request


post = []

@app.route('/')
@app.route('/index')
def index():
    if post: del post[:]
    return generate_view(post, '/')

@app.route('/', methods = ['POST'])
def field():
    text = request.form['post']
    print(text)
    post.append(text)
    return generate_view(post, '/')