import json
import os

# model
from core.models.Get_comment import Get_Comment

def get_all_commetns():
    """
    Возвращает все отзывы из all_comments.json
    """

    if not os.path.exists("./core/db/all_comments.json"):
        with open("./core/db/all_comments.json", "w", encoding="utf-8") as f:
            json.dump([], f)
    with open("./core/db/all_comments.json", "r+", encoding="utf-8") as f:
        data = json.load(f)
        return data

def get_ID_under_review_comments(id_to):
    """
    Ищет все отзывы о сотруднике
    возвращает массив отзывов на сотрудника и список сотрудников, которые написали о нем отзыв
    """

    if not os.path.exists("./core/db/all_comments.json"):
        with open("./core/db/all_comments.json", "w", encoding="utf-8") as f:
            json.dump([], f)
    with open("./core/db/all_comments.json", "r+", encoding="utf-8") as f:
        data = json.load(f)
        array = []
        users = []
        for i in data:
            if i["ID_under_review"] == id_to:
                array.append(i)
                if i["ID_reviewer"] not in users:
                    users.append(i["ID_reviewer"])

        return array, users

def get_ID_review_comment(id_to, id_from):
    """
    Поиск всех отзывов написанных одним сотрудником на другого сотрудника,
    Возвращает массив отзывов
    """
    
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
    """
    Конвертирует отзыв в словарь и добавляет его в all_comments.json
    """

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
    """
    Возвращает список, в котором объеденины все отзывы от одного сотрудника о другом сотруднике
    """
    
    merged_reviews = {}
    for review in reviews:
        reviewer_id = review["ID_reviewer"]
        if reviewer_id in merged_reviews:
            # Объединяем отзывы, добавляя новый текст к существующему
            merged_reviews[reviewer_id]["review"] += "\n" + review["review"] + " - " + str(review["date"])
        else:
            # Если ID_reviewer еще не встречался, добавляем отзыв в словарь
            merged_reviews[reviewer_id] = review
    
    # Преобразуем словарь обратно в список
    return list(merged_reviews.values())
