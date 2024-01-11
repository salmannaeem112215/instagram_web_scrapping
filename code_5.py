import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load cookies if saved, otherwise perform login
try:
    with open("instagram_cookies.json", "r") as cookies_file:
        cookies = json.load(cookies_file)
        for cookie in cookies:
            driver.add_cookie(cookie)
except FileNotFoundError:
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
    password_field.send_keys("MY PASSWORD")  # Replace with your actual password

    # 4. Submit the login form
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    # 5. Wait for login to complete (adjust timeout as needed)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "main"))
    )  # Replace with a more specific condition if needed

    # Save cookies for future use
    with open("instagram_cookies.json", "w") as cookies_file:
        json.dump(driver.get_cookies(), cookies_file)

# 6. Proceed with the rest of your code (assuming login is successful)
url = "https://www.instagram.com/explore/"
driver.get(url)

# ... (rest of your code)
