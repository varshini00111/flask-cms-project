import os
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

    image = request.files.get('image')
    image_url = None

    if image and image.filename != "":
        # Save locally (simple approach for project)
        filepath = os.path.join("app/static", image.filename)
        os.makedirs("app/static", exist_ok=True)
        image.save(filepath)

        image_url = "/" + filepath

    articles.append({
        'title': title,
        'author': author,
        'body': body,
        'image_url': image_url
    })

    logging.info("admin logged in successfully")

    return redirect('/')
