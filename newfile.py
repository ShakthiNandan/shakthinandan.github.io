from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os

# List of your sites
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
    "shakthinandan.onrender.com"
]

# Create output directory if it doesn't exist
output_dir = "screenshots"
os.makedirs(output_dir, exist_ok=True)

# Configure Selenium WebDriver (Headless Chrome)
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run without opening browser window
chrome_options.add_argument('--window-size=1920,1080')  # Set window size
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

# Path to chromedriver (update path if needed)
driver = webdriver.Chrome(options=chrome_options)

for site in sites:
    url = f"https://{site}"
    print(f"Visiting {url}")

    try:
        driver.get(url)
        time.sleep(5)  # Wait for 5 seconds for the page to load completely

        # Optionally: wait until body is loaded
        driver.find_element(By.TAG_NAME, "body")

        filename = site.split('.')[0] + ".png"  # Save with base name
        filepath = os.path.join(output_dir, filename)

        driver.save_screenshot(filepath)
        print(f"Saved screenshot: {filepath}")

    except Exception as e:
        print(f"Error visiting {url}: {e}")

driver.quit()
print("All screenshots captured!")