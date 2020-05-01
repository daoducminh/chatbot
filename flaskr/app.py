import os

from flask import Flask, send_from_directory

from flaskr.controllers.bot import bot

app = Flask(__name__)
app.register_blueprint(bot, url_prefix='/bot')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')


if __name__ == '__main__':
    app.run()
