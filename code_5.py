from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1. Navigate to the login page
driver = webdriver.Chrome()  # Replace with your preferred browser driver
url = "https://www.instagram.com/accounts/login/"
driver.get(url)

# 2. Locate username and password fields
username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
password_field = driver.find_element(By.NAME, "password")

# 3. Enter your login credentials
username_field.send_keys("salman.naeem.112215")  # Replace with your actual username
password_field.send_keys("MY PASSWORD ")  # Replace with your actual password

time.sleep(1)
# 4. Submit the login form
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()


time.sleep(5)

# 5. Wait for login to complete (adjust timeout as needed)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "main"))
)  # Replace with a more specific condition if needed

# 6. Proceed with the rest of your code
url = "https://www.instagram.com/explore/"
driver.get(url)



time.sleep(15)  # Consider using WebDriverWait for more robust waiting
