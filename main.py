import asyncio
from pathlib import Path
from browser import get_url
from dwnld import dwnld_video
from read_json import rd_js
from right_filename import clear_filename


async def main():
    data = rd_js("links.json")

    for video_id, video in data.items():
        
        section = video.get("section")
        name = video.get("name")
        link = video.get("link")

        safe_name = clear_filename(name)

        folder = Path(r"D:\Conference") / str(section)
        folder.mkdir(parents = True, exist_ok = True)

        output_path = folder / safe_name
        done_file = folder / f"{safe_name}.done"

        if done_file.exists():
            continue

        try:
            master_url = await get_url(link)

            dwnld_video(master_url, output_path) 

            done_file.touch()         

        except Exception as error:
            print(error)

            continue

asyncio.run(main())