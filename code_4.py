from selenium import webdriver
import time

driver = webdriver.Chrome()  # Replace with your preferred browser driver
url = "https://www.instagram.com/explore/topics/164724284439267/gothic-fashion/"
driver.get(url)

# Allow some time for initial loading (adjust as needed)
time.sleep(5)  # Consider using WebDriverWait for more robust waiting

# Download the HTML source immediately
with open("instagram_page.html", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

driver.quit()
