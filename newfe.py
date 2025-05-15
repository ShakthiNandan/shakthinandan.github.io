import requests

sites = [
# List of your hosted sites
    "shakthi.pythonanywhere.com",
    "shakthinandan7.pythonanywhere.com",
    "sssnandan.pythonanywhere.com",
    "aiandds.pythonanywhere.com",
    "usim.pythonanywhere.com",
    "treasurehuntcit.pythonanywhere.com",
    "vr-fpv-drone-aframe.onrender.com",
    "medme.onrender.com",
    "shakthinandan.onrender.com",

    "covid-chatbot-g11j.onrender.com",
    
    "CITLibrary.pythonanywhere.com"]

for site in sites:
    url = f"https://{site}"
    filename = f"{site.split('.')[0]}.png"
    print(f"Capturing screenshot of {url} -> {filename}")

    try:
        # Get full-page screenshot from thum.io
        response = requests.get(f"https://image.thum.io/get/fullpage/{url}")
        response.raise_for_status()

        # Save screenshot
        with open(filename, 'wb') as f:
            f.write(response.content)

        print(f"Saved {filename}")

    except Exception as e:
        print(f"Failed to capture {url}: {e}")