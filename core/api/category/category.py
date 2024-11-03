from fastapi import APIRouter, HTTPException
import json
from core.services.db_logic.all_comments import get_all_commetns
from core.services.db_logic.all_comments import get_person_comments
from core.services.db_logic.all_comments import filtr_com
from core.services.db_logic.sort_comments import get_comments_under_review_db
from core.services.db_logic.sort_comments import add_sort_comments_db
from core. services.prompts.all_prompts import short_prompt
from core. services.prompts.all_prompts import prepare_prompt

from core.services.moduls.modul import short_review
from core.services.moduls.modul import evaluate_reviews_with_llm


router = APIRouter()

@router.get("/categories")
def get_info():
    all_comments_data = get_all_commetns()
    return all_comments_data



@router.get("/categories/{id_to}/{com}")
def get_comments(id_to: int, com: str):
    comments_data = get_comments_under_review_db(id_to)
    if len(comments_data) == 0:
        data = get_person_comments(id_to)
        if len(data) == 0:
            raise HTTPException(status_code=404, detail="Нет данных в бд")
        filtered_data = filtr_com(data)
        
        for comment in filtered_data:
            prompt = short_prompt(comment)
            try:
                review_response = json.loads(short_review(prompt))
                comments_data.append(review_response)
                add_sort_comments_db(review_response["ID_reviewer"], review_response["ID_under_review"], review_response["review"])

            except Exception as e:
                print(f"Произошла ошибка: {e}")
                raise HTTPException(status_code=500, detail="Невозможно преобразовать данные")
    prompt = prepare_prompt(comments_data, com)
    return evaluate_reviews_with_llm(prompt)        
    
