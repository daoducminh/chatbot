from underthesea import word_tokenize
import time
from functools import reduce
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
from tensorflow.keras.layers import Dense, Flatten, Dropout
from tensorflow.keras.losses import CategoricalCrossentropy
from tensorflow.keras.models import Sequential
from utilities import read_pickle_file

if __name__ == "__main__":
    data = []
    labels = read_pickle_file('data/labels.pkl')
    documents = read_pickle_file('data/documents.pkl')
    bag_of_words = read_pickle_file('data/words.pkl')
    tags = read_pickle_file('data/tags.pkl')

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
    label_lb.fit(tags)
    train_labels = label_lb.transform(train_labels)
    test_labels = label_lb.transform(test_labels)

    model = Sequential(
        Dense(128, input_shape=(len(train_data[0]),), activation='relu'),
        Dense(64, activation='relu'),
        Dropout(0.5),
        Dense(len(train_labels[0]), activation='softmax')
    )

    model.compile(
        optimizer='sgd',
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
