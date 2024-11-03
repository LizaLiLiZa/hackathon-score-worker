import json
import os
from core.services.db_logic.all_comments import get_person_comments
from core.services.db_logic.all_comments import filtr_com
from core.services.prompts.all_prompts import short_prompt
from core.services.moduls.modul import short_review

def add_sort_comments_db(id_to, id_from, gen_comm):
    if not os.path.exists("./core/db/sort_comments.json"):
        with open("./core/db/sort_comments.json", "w", encoding="utf-8") as f:
            json.dump([], f)
    with open("./core/db/sort_comments.json", "r+", encoding="utf-8") as f:
        data = json.load(f) #get_sort_comments_db(id_to)
        print(data)
        data.append({"ID_reviewer": id_to, "ID_under_review": id_from, "review": gen_comm})
        f.seek(0)
        json.dump(data, f, indent=4, ensure_ascii=False)
    with open("./core/db/sort_comments.json", "r", encoding="utf-8") as f:
        print(json.load(f))


def get_comments_under_review_db(id_to):
    if not os.path.exists("./core/db/sort_comments.json"):
        return [] 
    with open("./core/db/sort_comments.json", "r+", encoding="utf-8") as f:
        data = json.load(f)
        filter_data = []
        for i in data:
            if i["ID_under_review"] == id_to:
                filter_data.append(i)
        return filter_data
"""
com = get_comments_under_review_db(6135)
print(com)

com = filtr_com(com)
for i, r in enumerate(com, start=1):
    prompt_new = short_prompt(r)
    ans = short_review(prompt_new)
    print(ans)"""