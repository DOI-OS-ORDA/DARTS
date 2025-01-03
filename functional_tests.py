from selenium import webdriver
from selenium.webdriver.firefox.options import Options
options = Options()
options.binary_location = r'/usr/bin/firefox-esr'
options.add_argument("--no-sandbox")
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
from selenium.webdriver.firefox.service import Service
service = Service('/usr/local/bin/geckodriver')
browser = webdriver.Firefox(options=options, service=service)

browser.get("http://web:8000")

assert "Search • DARTS" in browser.title, f"Got: {browser.title}"
print("OK")
