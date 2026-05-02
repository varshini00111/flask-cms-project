from flask import Blueprint, render_template, request, redirect
import logging

main = Blueprint('main', __name__)

articles = []

@main.route('/')
def index():
    return render_template('index.html', articles=articles)

@main.route('/create', methods=['POST'])
def create():
    title = request.form['title']
    author = request.form['author']
    body = request.form['body']

    # Login check
    username = request.form.get('username')
    password = request.form.get('password')

    if username == "admin" and password == "pass":
        logging.info("admin logged in successfully")
    else:
        logging.warning("Invalid login attempt")

    articles.append({
        'title': title,
        'author': author,
        'body': body
    })

    return redirect('/')
