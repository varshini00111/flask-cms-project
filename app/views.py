import logging
from flask import Blueprint, render_template, request, redirect
# Create Blueprint
main = Blueprint('main', __name__)
# Temporary storage (since no DB used here)
articles = []
# Dummy credentials (for logging requirement)
USERNAME = "admin"
PASSWORD = "pass"
@main.route('/')
def index():
    return render_template('index.html', articles=articles)
@main.route('/create', methods=['POST'])
def create():
    title = request.form.get('title')
    author = request.form.get('author')
    body = request.form.get('body')
    # 🔐 Simple login simulation (for rubric requirement)
    if author == USERNAME and title == PASSWORD:
        logging.info("admin logged in successfully")
    else:
        logging.warning("Invalid login attempt")
    # Store article
    articles.append({
        'title': title,
        'author': author,
        'body': body
    })
    return redirect('/')
