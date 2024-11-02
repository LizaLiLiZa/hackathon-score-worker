import json
import os

def get_comm_add(id_to, id_from, gen_comm):
    if not os.path.exists("gen_comm.json"):
        with open("gen_comm.json", "w", encoding="utf-8") as f:
            json.dump([], f)

    with open("gen_comm.json", "r+", encoding="utf-8") as f:
        data = json.load(f)
        data.append({"id_to": id_to, "id_from": id_from, "gen_comm": gen_comm})
        f.seek(0)
        json.dump(data, f, indent=4)


    with open("gen_comm.json", "r", encoding="utf-8") as f:
        print(json.load(f))
