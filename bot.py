from underthesea import word_tokenize, pos_tag
import pickle
from functools import reduce
from tensorflow.keras.models import load_model
from sklearn.preprocessing import LabelBinarizer
import numpy as np
from utilities import read_pickle_file

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


def classify_question(question):
    temp = word_tokenize(question)
    temp = [w.lower().replace('_', ' ')
            for w in temp if w in bag_of_words]

    temp = data_lb.transform(temp)
    temp = reduce(np.add, list(temp))

    predictions = model.predict(np.array([temp]))
    return list(label_lb.inverse_transform((predictions > 0.5).astype(int)))


if __name__ == "__main__":
    question = 'giày adidas nam'
    print(classify_question(question))
