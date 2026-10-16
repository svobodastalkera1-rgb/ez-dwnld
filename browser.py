import asyncio
from geturl import get_master_url
from playwright.async_api import async_playwright


async def get_url(page_url):
    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir="browser_profile",
            headless=False
        )

        page = await context.new_page()

        master_url = await get_master_url(
            page,
            page_url
        )

        print("Master:")
        print(master_url)

        await context.close()
    
        return(master_url) 