from pyvi import ViTokenizer
import json
import time
import pickle
from functools import reduce
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
from tensorflow.keras.layers import Dense, Dropout, Flatten, Bidirectional, LSTM
from tensorflow.keras.losses import CategoricalCrossentropy
from tensorflow.keras.models import Sequential

data = []
labels = []
documents = []
ignore_words = ['?', '!', ',', 'có', 'có thể',
                'gì', 'đi', 'đó', 'xin', 'đế', 'ơi', 'ạ', 'ở', 'thì',
                'từ', 'shop', 'nhỉ', 'như', 'những', 'mẫu', 'mình',
                'muốn', 'hỏi', 'của', 'chút', 'cho']
# brands = [
#     'nike',
#     'adidas',
#     'new nalance',
#     'skechers',
#     'asics',
#     'avia'
# ]


def filter_stopword(word):
    if word in ignore_words:
        return False
    return True


bag_of_words = []
with open('data/intents2.json')as file:
    intents = json.load(file)
    for intent in intents:
        tag = intent['tag']
        for pattern in intent['patterns']:
            temp = ViTokenizer.tokenize(pattern)
            pattern_words = [w.lower().replace('_', ' ')
                             for w in temp.split(' ') if filter_stopword(w)]
            bag_of_words.extend(pattern_words)
            documents.append(pattern_words)
            labels.append(tag)

bag_of_words = sorted(list(set(bag_of_words)))
with open('data/words.pkl', 'wb') as file:
    pickle.dump(bag_of_words, file)
with open('data/tags.pkl', 'wb') as file:
    pickle.dump(sorted(list(set(labels))), file)

data_lb = LabelBinarizer()
data_lb.fit(bag_of_words)
for doc in documents:
    temp = data_lb.transform(doc)
    temp = reduce(np.add, list(temp))
    data.append(temp)
data = np.array(data)
labels = np.array(labels)


(train_data, test_data, train_labels, test_labels) = train_test_split(
    data, labels, test_size=0.2)

# train_data = data
# test_data = data
# train_labels = labels
# test_labels = labels

label_lb = LabelBinarizer()
label_lb.fit(labels)
train_labels = label_lb.transform(train_labels)
test_labels = label_lb.transform(test_labels)

model = Sequential()
model.add(Dense(128, input_shape=(len(train_data[0]),), activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_labels[0]), activation='softmax'))

model.compile(
    optimizer='adamax',
    loss=CategoricalCrossentropy(),
    metrics=['accuracy']
)

time_start = time.time()

history = model.fit(
    train_data,
    train_labels,
    epochs=50,
    batch_size=5,
    validation_data=(test_data, test_labels),
    verbose=2
)

time_end = time.time()
print('Training time:', time_end - time_start)

test_loss, test_acc = model.evaluate(test_data,  test_labels, verbose=2)
print(test_acc, test_loss)

model.save('saved_models/model_1')
