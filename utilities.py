import pickle


ignore_words = ['?', '!', ',', '.', 'có', 'có thể',
                'gì', 'đi', 'đó', 'xin', 'đế', 'ơi', 'ạ', 'ở', 'thì',
                'từ', 'shop', 'nhỉ', 'như', 'những', 'mẫu', 'mình',
                'muốn', 'hỏi', 'của', 'chút', 'cho', 'mình', 'xem',
                'thích', 'tìm', 'nào', 'tôi', 'của', 'mấy', 'đang',
                'nhu cầu', 'mua', 'làm']
BRANDS = [
    'nike',
    'adidas',
    'new balance',
    'skechers',
    'asics',
    'avia'
]


def filter_stopword(word):
    if word in ignore_words:
        return False
    return True


def read_pickle_file(filepath):
    with open(filepath, 'rb') as file:
        return pickle.load(file)


def write_pickle_file(filepath, obj):
    with open(filepath, 'wb') as file:
        return pickle.dump(obj, file)
