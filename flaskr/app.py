import os

from dotenv import load_dotenv
from flask import Flask, render_template, send_from_directory
from flaskr.controllers.bot import bot
from pymongo import MongoClient

load_dotenv(dotenv_path='.env')
MONGODB_URI = os.getenv('MONGODB_URI')

app = Flask(__name__)
app.register_blueprint(bot, url_prefix='/bot')

client = MongoClient(MONGODB_URI)
collection = client['nlp']['test']


@app.route('/')
def home():
    result = collection.find({})
    result = list(result)
    for r in result:
        del r['_id']
        r['colors'] = ', '.join(r['colors'])
        r['sizes'] = ', '.join([str(x) for x in r['sizes']])
    return render_template('index.html', items=result)


@ app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')


if __name__ == '__main__':
    app.run()
