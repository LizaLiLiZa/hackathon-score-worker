import json
import requests
from pydantic import BaseModel
from core.services.db_logic.all_comments import get_person_comments
from core.services.db_logic.all_comments import filtr_com
from core.services.prompts.all_prompts import short_prompt

class Review(BaseModel):
    ID_reviewer: int
    ID_under_review: int
    review: str

def short_review(prompt):
    url = "https://vk-scoreworker-case-backup.olymp.innopolis.university/generate"

    data = {
        "prompt": [prompt],
        "apply_chat_template": True,
        "system_prompt": "You are a smart assistant who should evaluate the personal qualities of employees based on reviews",
        "max_tokens": 1000,
        "n": 1,
        "temperature": 0.89,
        # "lenght_penalty": 0.8,
        #"seed": 42,  # для тестирования
        "schema": Review.model_json_schema(),
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url,  data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code} - {response.text}"
    

def evaluate_reviews_with_llm(prompt):
    url = "https://vk-scoreworker-case-backup.olymp.innopolis.university/generate"
    data = {
        "prompt": [prompt],
        "apply_chat_template": True,
        "system_prompt": "You are a smart assistant who should evaluate the personal qualities of employees based on reviews.",
        "max_tokens": 1000,
        "n": 1,
        "temperature": 0.4, 
        "seed": 42,  # для тестирования
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code} - {response.text}"