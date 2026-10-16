import json


def rd_js(file_path):
    with open (file_path, "r", encoding = "utf-8") as file:
        data = json.load(file)

    return data