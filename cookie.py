import asyncio
from pyppeteer import launch

async def get_cookies():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://www.google.com')
    cookies = await page.cookies()
    await browser.close()
    return cookies

# Run the asyncio event loop
cookies = asyncio.get_event_loop().run_until_complete(get_cookies())

# Print the session cookies
for cookie in cookies:
    print(f'{cookie["name"]}: {cookie["value"]}')