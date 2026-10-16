import json
from pathlib import Path


with open ("links.json", "r", encoding = "utf-8") as file:
    data = json.load(file)

for video_id, video in data.items():
    
    section = video["section"]

    folder = Path("download") / str(section)
    folder.mkdir(parents = True, exist_ok = True)