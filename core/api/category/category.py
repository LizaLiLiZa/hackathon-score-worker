from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi import status

import json
import re
import datetime

# db
"""
    Подключение к сервису, работующему со всеми отзывами
"""
from core.services.db_logic.all_comments import get_all_commetns
from core.services.db_logic.all_comments import get_ID_under_review_comments
from core.services.db_logic.all_comments import get_ID_review_comment
from core.services.db_logic.all_comments import filtr_com
from core.services.db_logic.all_comments import add_all_comments

"""
    Подключение к сервису, работующему с мениями пользователей о людях
"""
from core.services.db_logic.sort_comments import get_comments_under_review_db
from core.services.db_logic.sort_comments import add_sort_comments_db

"""
    Подключение к генератором запросов
"""
from core. services.prompts.all_prompts import short_prompt
from core. services.prompts.all_prompts import prepare_prompt


"""
    Подключение к модулям
"""
from core.services.moduls.modul import short_review
from core.services.moduls.modul import evaluate_reviews_with_llm
from core.services.moduls.modul import is_valid_russian_text

"""
    Подключение к модулям
"""
from core.models.Get_comment import Get_Comment


router = APIRouter()


"""
    Возвращает все записи 
"""
@router.get("/categories")
def get_info():
    all_comments_data = get_all_commetns()
    return all_comments_data



@router.get("/categories/{id_to}/{com}/{Identificator}")
def get_comments(id_to: int, com: str, Identificator: bool):
    if Identificator == True or com == "" or com == " ":
        com = "1. Командная работа /n2. Вежливотсь /n3. Отзывчивость"
    comments_data = get_comments_under_review_db(id_to)
    data, users = get_ID_under_review_comments(id_to)
    if len(comments_data) == 0 or len(comments_data) != len(users):
        if len(data) == 0:
            raise HTTPException(status_code=404, detail="Нет данных в бд")
        filtered_data = filtr_com(data)

        print()
        for comment in filtered_data:
            print(comment)
            print()
            prompt = short_prompt(comment)            
            try:
                
                review_response = short_review(prompt)
                review_response = {"ID_reviewer": comment["ID_reviewer"], "ID_under_review": comment["ID_under_review"], "review": review_response}

                comments_data.append(review_response)
                add_sort_comments_db(review_response["ID_reviewer"], review_response["ID_under_review"], review_response["review"])

            except Exception as e:
                print(f"Произошла ошибка: {e}")
                raise HTTPException(status_code=500, detail="Невозможно преобразовать данные")
    prompt = prepare_prompt(comments_data, com)
    return evaluate_reviews_with_llm(prompt)


@router.post("/new-comment")
def post_comment(comment: Get_Comment):
    comment = dict(comment)
    comment["date"] = datetime.date.today().strftime("%m/%d/%Y")
    add_all_comments(comment)
    comment = get_ID_review_comment(comment["ID_under_review"], comment["ID_reviewer"])
    comment = filtr_com(comment)[0]
    prompt = short_prompt(comment)
    
    if is_valid_russian_text(comment):
        print("Присутствуют не кириллические символы")
        raise HTTPException(status_code=400, detail="В отзыве присутствуют не кириллические символы.")

    try:
        review_response = short_review(prompt)
        print(type(review_response))
        if review_response == "Нейтральный отзыв." or review_response == "Нейтральная оценка":
            print(0)
            raise HTTPException(status_code=422, detail="Некорректные данные: ожидается объективный отзыв, оценивающий некоторые качества сотрюдника, которые могут повлиять на рабочий процесс.")
        review_response = {"ID_reviewer": comment["ID_reviewer"], "ID_under_review": comment["ID_under_review"], "review": review_response}
        add_sort_comments_db(review_response["ID_reviewer"], review_response["ID_under_review"], review_response["review"])
        print(review_response)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        raise HTTPException(status_code=500, detail="Невозможно преобразовать данные")
    return review_response