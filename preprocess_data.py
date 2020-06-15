from underthesea import word_tokenize
import json
from utilities import write_pickle_file, filter_stopword

if __name__ == "__main__":
    with open('data/intents.json')as file:
        intents = json.load(file)
        bag_of_words = []
        documents = []
        labels = []
        for intent in intents:
            tag = intent['tag']
            for pattern in intent['patterns']:
                temp = word_tokenize(pattern)
                pattern_words = [
                    w.lower().replace('_', ' ')
                    for w in temp
                    if filter_stopword(w.lower() and w)
                ]
                if pattern_words:
                    bag_of_words.extend(pattern_words)
                    documents.append(pattern_words)
                    labels.append(tag)
        write_pickle_file('data/documents.pkl', documents)
        write_pickle_file('data/labels.pkl', labels)
        write_pickle_file('data/words.pkl', sorted(list(set(bag_of_words))))
        write_pickle_file('data/tags.pkl', sorted(list(set(labels))))
        write_pickle_file('data/intents.pkl', intents)
