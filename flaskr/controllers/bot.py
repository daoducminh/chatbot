from flask import Blueprint

bot = Blueprint('bot', __name__)


@bot.route('/')
def test():
    return 'Hello'
