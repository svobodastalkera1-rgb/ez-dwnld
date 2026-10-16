import asyncio
from playwright.async_api import async_playwright

PAGE_URL = "https://online.sochi-conference.ru/r/46"

async def main():
    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir = "browser_profile",
            headless = False
        )

        page = await context.new_page()

        async def request(response):
            url = response.url

            if "master" in url.lower() and ".m3u8" in url.lower():
                print("MASTER:")
                print(url)

        page.on("response", request)
        await page.goto(PAGE_URL)

        await page.wait_for_timeout(2000)

        await page.locator("KinescopeLayout-1c8hk4r _1jqyhyu  ").click()

        await context.close()

asyncio.run(main())