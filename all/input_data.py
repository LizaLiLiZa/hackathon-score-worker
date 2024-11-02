import json

def load_reviews(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reviews = json.load(file)
    return reviews
