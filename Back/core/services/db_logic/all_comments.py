import json
import os

# model
from core.models.Get_comment import Get_Comment

def get_all_commetns():
    if not os.path.exists("./core/db/all_comments.json"):
        with open("./core/db/all_comments.json", "w", encoding="utf-8") as f:
            json.dump([], f)
    with open("./core/db/all_comments.json", "r+", encoding="utf-8") as f:
        data = json.load(f)
        return data

def get_ID_under_review_comments(id_to):
    if not os.path.exists("./core/db/all_comments.json"):
        with open("./core/db/all_comments.json", "w", encoding="utf-8") as f:
            json.dump([], f)
    with open("./core/db/all_comments.json", "r+", encoding="utf-8") as f:
        data = json.load(f)
        array = []
        for i in data:
            if i["ID_under_review"] == id_to:
                array.append(i)
        return array

def get_ID_review_comment(id_to, id_from):
    if not os.path.exists("./core/db/all_comments.json"):
        with open("./core/db/all_comments.json", "w", encoding="utf-8") as f:
            json.dump([], f)
    with open("./core/db/all_comments.json", "r+", encoding="utf-8") as f:
        data = json.load(f)
        array = []
        for i in data:
            if i["ID_under_review"] == id_to and i["ID_reviewer"] == id_from:
                array.append(i)
        return array
    
def add_all_comments(comment: Get_Comment):
    if not os.path.exists("./core/db/all_comments.json"):
        with open("./core/db/all_comments.json", "w", encoding="utf-8") as f:
            json.dump([], f)
    with open("./core/db/all_comments.json", "r+", encoding="utf-8") as f:
        data = json.load(f)
        if type(comment) != dict:
            comment = dict(comment)
        data.append(comment)
        f.seek(0)
        json.dump(data, f, indent=4, ensure_ascii=False)


def filtr_com(reviews):
    merged_reviews = {}
    for review in reviews:
        reviewer_id = review["ID_reviewer"]
        if reviewer_id in merged_reviews:
            # Объединяем отзывы, добавляя новый текст к существующему
            merged_reviews[reviewer_id]["review"] += "\n" + review["review"]
        else:
            # Если ID_reviewer еще не встречался, добавляем отзыв в словарь
            merged_reviews[reviewer_id] = review
    
    # Преобразуем словарь обратно в список
    return list(merged_reviews.values())
