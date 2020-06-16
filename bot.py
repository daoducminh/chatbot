import os
from functools import reduce
from random import randrange

import numpy as np
from pymongo import MongoClient
from sklearn.preprocessing import LabelBinarizer
from tensorflow.keras.models import load_model
from underthesea import pos_tag, word_tokenize

from utilities import filter_stopword, read_pickle_file

BRAND = 'brand'
GENDER = 'gender'
COLOR = 'color'
SIZE = 'size'
MEN = 'nam'
WOMEN = 'nữ'
MONGODB_URI = os.getenv('MONGODB_URI')

client = MongoClient(MONGODB_URI)
collection = client['nlp']['test']

intents = read_pickle_file('data/intents.pkl')
# Load trained model
model = load_model('saved_models/model_1')
# Load bag of words and tags
bag_of_words = read_pickle_file('data/words.pkl')
tags = read_pickle_file('data/tags.pkl')

# Initialize LabelBinarizer
data_lb = LabelBinarizer()
data_lb.fit(bag_of_words)
label_lb = LabelBinarizer()
label_lb.fit(tags)


def classify_question(tokens):
    temp = [w.lower().replace('_', ' ')
            for w in tokens if w.lower() in bag_of_words]

    try:
        temp = data_lb.transform(temp)
        temp = reduce(np.add, list(temp))

        predictions = model.predict(np.array([temp]))
        return list(label_lb.inverse_transform((predictions > 0.5).astype(int)))
    except:
        return ['noanswer']


def handle_question(tag, tokens, question):
    for intent in intents:
        if tag == intent['tag']:
            if intent['responses']:
                return (True, intent['responses'][randrange(0, len(intent['responses']))])
            else:
                temp_tokens = [
                    w for w in tokens
                    if filter_stopword(w.lower()) and w
                ]
                temp = pos_tag(' '.join(temp_tokens))

                labels = intent['labels']
                query = {}
                brand_query = {}
                gender_query = {}
                color_query = {}
                size_query = {}
                if BRAND in labels:
                    brands = []
                    for t in temp:
                        if t[1] == 'Np':
                            brands.append({'brand': t[0]})
                    brand_query['$or'] = brands
                if GENDER in labels:
                    genders = []
                    if MEN in temp_tokens:
                        genders.append({'categories': MEN})
                    if WOMEN in temp_tokens:
                        genders.append({'categories': WOMEN})
                    gender_query['$or'] = genders
                if COLOR in labels:
                    colors = []
                    for t in temp:
                        if t[1] == 'A':
                            colors.append({'colors': t[0]})
                    color_query['$or'] = colors
                if SIZE in labels:
                    sizes = []
                    for t in temp:
                        if t[1] == 'M':
                            try:
                                sizes.append({'sizes': int(t[0])})
                            except:
                                continue
                    size_query['$or'] = sizes
                query['$and'] = [
                    brand_query,
                    gender_query,
                    color_query,
                    size_query
                ]
                print(query)
                result = collection.find(query)
                return (False, list(result))
    return (True, 'Có lỗi đã xảy ra. Xin vui lòng thử lại.')


def respond(question):
    tokens = word_tokenize(question)
    tag = classify_question(tokens)[0]
    return handle_question(tag, tokens, question)
