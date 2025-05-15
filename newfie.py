import asyncio
from pyppeteer import launch
import os

# List of websites to visit
sites = [
    "shakthi.pythonanywhere.com",
    "shakthinandan7.pythonanywhere.com",
    "sssnandan.pythonanywhere.com",
    "aiandds.pythonanywhere.com",
    "usim.pythonanywhere.com",
    "treasurehuntcit.pythonanywhere.com",
    "covid-chatbot-cm6k.onrender.com",
    "vr-fpv-drone-aframe.onrender.com",
    "medme.onrender.com",
    "shakthinandan.onrender.com",
    "CITLibrary.pythonanywhere.com",
]

# Create a folder for screenshots
os.makedirs("screenshots", exist_ok=True)

async def capture_site(site):
    url = f"https://{site}"
    filename = f"screenshots/{site.split('.')[0]}.png"

    browser = await launch(
        headless=True,
        args=['--no-sandbox', '--disable-gpu']
    )
    page = await browser.newPage()
    await page.setViewport({'width': 1280, 'height': 800})
    print(f"Opening {url}")
    try:
        await page.goto(url, {'waitUntil': 'networkidle2', 'timeout': 60000})
        await asyncio.sleep(3)  # Ensure all assets load
        await page.screenshot({'path': filename, 'fullPage': True})
        print(f"Saved screenshot as {filename}")
    except Exception as e:
        print(f"Error with {url}: {e}")
    await browser.close()

async def main():
    for site in sites:
        await capture_site(site)

# Run the script
asyncio.get_event_loop().run_until_complete(main())#