from flask import Blueprint

bot = Blueprint('bot', __name__)


@bot.route('/init')
def init_chat_session():
    pass


@bot.route('/chat')
def chat(text):
    pass
