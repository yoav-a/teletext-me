import os
from flask import Flask, render_template
from requests import get, post

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('layout.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0',use_reloader=True, port=port)