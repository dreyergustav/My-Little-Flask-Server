import logging
import os

from flask import Flask

logging.basicConfig(filename=os.environ.get('FLASK_LOG_PATH', '/tmp/flask.log') ,level=logging.INFO)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
