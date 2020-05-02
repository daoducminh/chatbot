from flask import Blueprint, session, request
import uuid
import datetime

from flaskr.config.mongodb import mongo

bot = Blueprint('bot', __name__)


@bot.route('/init')
def init_chat_session():
    session['user'] = uuid.uuid4()
    return 'Initialized'


@bot.route('/all')
def test_session():
    return f"{session['user']}"


@bot.route('/chat', methods=['post'])
def chat():
    data = request.get_json()
    mongo.db[str(session['user'])].insert({
        'text': data['text'],
        'datetime': datetime.datetime.utcnow()
    })
    return 'received'


@bot.route('/')
def test():
    return 'tested'
