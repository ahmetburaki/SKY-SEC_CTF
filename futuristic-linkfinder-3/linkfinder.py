import asyncio
from pyppeteer import launch
import sys
import os
import random

file_name = os.getrandom(32).hex()

async def main():
    browser = await launch(
        {
            "executablePath": '/opt/chromium/chrome',
            "ignoreHTTPSErrors": True,
            "args": ["--no-sandbox"],
            "headless": True,
            "test-type": True,
            }
        );
    page = await browser.newPage()
    await page.goto(sys.argv[1])

    # find links in the website and return
    links = await page.evaluate('''() => {
        return Array.from(document.links).map(a => a.href);
    }''')

    with open(f"links/{file_name}.txt", "w") as f:
        f.write("\n".join(links))

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())

print(f"links/{file_name}.txt")
