from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# Set up the Service for geckodriver
service = Service(GeckoDriverManager().install())

# Set up the Firefox driver
driver = webdriver.Firefox(service=service)

# Open a website
driver.get("https://www.example.com")

# Keep the browser open for 5 seconds
import time
time.sleep(5)

# Close the browser
driver.quit()
