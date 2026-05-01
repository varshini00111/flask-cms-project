from flask import Flask, render_template, request, redirect

app = Flask(__name__)

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

    return redirect('/')

if __name__ == '__main__':
    app.run()
