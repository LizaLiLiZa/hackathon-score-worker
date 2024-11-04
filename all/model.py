import requests
import json


# В файле описана передача запросов к модели.


# Получить общую оценку.
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


# получить сокращенные отзывы
def short_review(prompt):
    url = "https://vk-scoreworker-case-backup.olymp.innopolis.university/generate"

    data = {
        "prompt": [prompt],
        "apply_chat_template": True,
        "system_prompt": "You are a smart assistant who should evaluate the personal qualities of employees based on reviews",
        "max_tokens": 1000,
        "n": 1,
        "temperature": 0.4,
        "length_penalty": 1.5,
        "seed": 42,  # для тестирования
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
    

# Получить набор критериев.
def criteria_review(prompt):
    url = "https://vk-scoreworker-case-backup.olymp.innopolis.university/generate"

    data = {
        "prompt": [prompt],
        "apply_chat_template": True,
        "system_prompt": "You are a smart assistant who should evaluate the personal qualities of employees based on reviews",
        "max_tokens": 1000,
        "n": 1,
        "temperature": 0.2,
        "length_penalty": 1.5,
        "seed": 42,  # для тестирования
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url,  data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code} - {response.text}"