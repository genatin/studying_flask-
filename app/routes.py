from app import app
from generating_view import generate_view
from flask import request


post = []

@app.route('/')
@app.route('/index')
def index():
    return generate_view([], '/field')

@app.route('/field', methods = ['POST'])
def field():
    text = request.form['post']
    post.append(text)
    return generate_view(post, '/field', default_text='')