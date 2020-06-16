import os

from flask import Blueprint, jsonify, request
from pymongo import MongoClient

from bot import respond

MONGODB_URI = os.getenv('MONGODB_URI')

bot = Blueprint('bot', __name__)
client = MongoClient(MONGODB_URI)
collection = client['nlp']['test']


@bot.route('/', methods=['POST'])
def chat():
    data = request.get_json()
    question = data['text']
    result = respond(question)
    if result[0]:
        return jsonify({'text': result[1]}), 200
    else:
        if result[1]:
            temp = result[1]
            for r in temp:
                del r['_id']
                r['colors'] = ','.join(r['colors'])
                r['sizes'] = ', '.join([str(x) for x in r['sizes']])
            return jsonify({
                'text': 'Tìm được các kết quả',
                'items': temp
            }), 200
        else:
            return jsonify({'text': 'Không tìm được kết quả nào phù hợp'}), 200
