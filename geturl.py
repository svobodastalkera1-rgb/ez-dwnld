import asyncio

async def get_master_url(page, page_url):
    m3u8_found = asyncio.Event()
    found_url = None

    async def handle_response(response):
        nonlocal found_url
                
        url = response.url

        if "master.m3u8" in url.lower():
            found_url = url
            m3u8_found.set()
        
    page.on("response", handle_response)

    await page.goto(page_url)
    await page.wait_for_timeout(3000)

    kinescope_frame = None
        
    for frame in page.frames:
        if "kinescope.io" in frame.url.lower():
            kinescope_frame = frame
            break

    if kinescope_frame is None:
        raise RuntimeError("Kinescope iframe не найден")

    play_button = kinescope_frame.locator("button").first

    print(
        "Найдена кнопка:",
        await play_button.get_attribute("aria-label")
    )

    await play_button.click()

    try:
        await asyncio.wait_for(
            m3u8_found.wait(),
            timeout = 15
        )

    except asyncio.TimeoutError:
        raise RuntimeError("master.m3u8 не найден")

    return found_url