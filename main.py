import asyncio
from pathlib import Path
from test import get_url
from dwnld import dwnld_video
from read_json import rd_js


async def main():
    data = rd_js("links.json")

    for video_id, video in data.items():
        
        section = video.get("section")
        name = video.get("name")
        link = video.get("link")

        folder = Path("download") / str(section)
        folder.mkdir(parents = True, exist_ok = True)

        master_url = await get_url(link)

        dwnld_video(master_url, folder / name)          

    master_url = await get_url()

    dwnld_video(
        master_url,
        folder / name
    )

asyncio.run(main())