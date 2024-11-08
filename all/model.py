import requests
import json



def evaluate_reviews_with_llm(prompt):
    url = "https://vk-scoreworker-case-backup.olymp.innopolis.university/generate"
    data = {
        "prompt": [prompt],
        "apply_chat_template": True,
        "system_prompt": "You are a helpful assistant.",
        "max_tokens": 1000,
        "n": 1,
        "temperature": 0.7
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code} - {response.text}"
    