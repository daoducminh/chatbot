from underthesea import word_tokenize, pos_tag
from functools import reduce
from tensorflow.keras.models import load_model
from sklearn.preprocessing import LabelBinarizer
import numpy as np
from utilities import read_pickle_file, filter_stopword
from random import randrange

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
            for w in tokens if w in bag_of_words]

    try:
        temp = data_lb.transform(temp)
        temp = reduce(np.add, list(temp))

        predictions = model.predict(np.array([temp]))
        return list(label_lb.inverse_transform((predictions > 0.5).astype(int)))
    except:
        return ['noanswer']


def respond(tag, tokens):
    for intent in intents:
        if tag == intent['tag']:
            if intent['responses']:
                return intent['responses'][randrange(0, len(intent['responses']))]
            else:
                temp = 1
                tagged_sentence = pos_tag(question)
    return 'Có lỗi đã xảy ra. Xin vui lòng thử lại.'


if __name__ == "__main__":
    # question = 'abc ajdkf xcjvlkaaf'
    question = 'giày New Balance nam màu đỏ cỡ 31'
    tokens = word_tokenize(pattern)
    tag = classify_question(question)[0]
    # print(tag)
    r = respond(tag, tokens)
    print(r)
