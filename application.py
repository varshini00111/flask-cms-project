from flask import Flask, render_template, request, redirect
import logging

app = Flask(__name__)

# 🔹 Enable logging
logging.basicConfig(level=logging.INFO)

articles = []

@app.route('/')
def index():
    return render_template('index.html', articles=articles)

@app.route('/create', methods=['POST'])
def create():
    title = request.form['title']
    author = request.form['author']
    body = request.form['body']

    articles.append({
        'title': title,
        'author': author,
        'body': body
    })

    # 🔹 SUCCESS LOG
    logging.info("Article created successfully")

    return redirect('/')

# 🔹 TEST WARNING LOG (for screenshot)
logging.warning("Invalid login attempt")

if __name__ == '__main__':
    app.run()
