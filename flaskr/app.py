import os
from flask import Flask, send_from_directory, render_template
from flaskr.config.connections import MONGO_URI
from flaskr.config.keys import *

app = Flask(__name__)
app.secret_key = SESSION_KEY
app.config["MONGO_URI"] = MONGO_URI

from flaskr.controllers.bot import bot

app.register_blueprint(bot, url_prefix='/bot')


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')


if __name__ == '__main__':
    app.run()
