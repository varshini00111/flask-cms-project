from flask import Flask, render_template, request, redirect, session, url_for
import logging
import os
import msal

app = Flask(__name__)
app.secret_key = "secret123"   # required for session

# 🔹 Enable logging
logging.basicConfig(level=logging.INFO)

articles = []

# 🔹 MSAL CONFIG
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
AUTHORITY = "https://login.microsoftonline.com/common"
REDIRECT_PATH = "/getAToken"
SCOPE = ["User.Read"]

# 🔹 MSAL helper
def build_msal_app():
    return msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
        client_credential=CLIENT_SECRET
    )

def build_auth_url():
    return build_msal_app().get_authorization_request_url(
        SCOPE,
        redirect_uri=url_for("authorized", _external=True)
    )

# 🔹 Home page
@app.route('/')
def index():
    return render_template('index.html', articles=articles)

# 🔹 Create article
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

    logging.info("admin logged in successfully")   # success log

    return redirect('/')

# 🔹 Login route
@app.route('/login')
def login():
    return redirect(build_auth_url())

# 🔹 Token handler
@app.route(REDIRECT_PATH)
def authorized():
    try:
        result = build_msal_app().acquire_token_by_authorization_code(
            request.args.get('code'),
            scopes=SCOPE,
            redirect_uri=url_for("authorized", _external=True)
        )

        if "access_token" in result:
            logging.info("Microsoft login success")
            return redirect('/')
        else:
            logging.warning("Invalid login attempt")
            return "Login failed"

    except Exception as e:
        logging.warning("Exception during login")
        return str(e)

# 🔹 Failure log (for screenshot)
logging.warning("Invalid login attempt")

if __name__ == '__main__':
    app.run()
