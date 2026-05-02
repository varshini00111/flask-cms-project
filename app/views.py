from flask import Blueprint, render_template, request, redirect
import os

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
        os.makedirs("app/static", exist_ok=True)

        filepath = os.path.join("app/static", image.filename)
        image.save(filepath)

        image_url = "/static/" + image.filename

    articles.append({
        'title': title,
        'author': author,
        'body': body,
        'image_url': image_url
    })

    return redirect('/')
