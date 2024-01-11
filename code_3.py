from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()  # Replace with your preferred browser driver
url = "https://www.instagram.com/explore/topics/164724284439267/gothic-fashion/"
driver.get(url)

print("JOO")
# Wait for reels to load (adjust timeout as needed)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "main"))
)
print("JO2")

# Access reel elements and extract data (example)
reel_items = driver.find_elements(By.CLASS_NAME, "ReelMediaItem")
print("JO3")
for reel in reel_items:
    thumbnail_url = reel.find_element(By.TAG_NAME, "img").get_attribute("src")
    print(thumbnail_url)

driver.quit()
