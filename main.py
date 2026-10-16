import asyncio
from pathlib import Path
from test import get_url
from dwnld import dwnld_video

    
async def main():

    output_path = Path("download") / "test_video"

    master_url = await get_url()

    dwnld_video(
        master_url,
        output_path
    )

asyncio.run(main())