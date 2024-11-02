import json
import os

def gen_comm_add(id_to, id_from, gen_comm):
    if not os.path.exists("gen_comm.json"):
        try:
            with open("gen_comm.json", "w", encoding="utf-8") as f:
                json.dump([], f)
        except IOError as e:
            print("Ошибка при создании файла:{e}")
    try:
        with open("gen_comm.json", "r+", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print("Ошибка чтения из json файла! Файл может быть поврежден!")     
            data.append({"id_to": id_to, "id_from": id_from, "gen_comm": gen_comm})
            f.seek(0)
            try:
                json.dump(data, f, indent=4)
            except IOError as e:
                print("Ошибка при записи данных в файл:{e}")
    except IOError as e:
            print("Ошибка при чтении/записи данных в файл:{e}")




    with open("gen_comm.json", "r", encoding="utf-8") as f:
        print(json.load(f))
