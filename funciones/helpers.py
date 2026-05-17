from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver 

def login(driver, username, password):

    wait = WebDriverWait(driver , 10)

    driver.get("https://www.saucedemo.com/")

    wait.until(
        EC.presence_of_element_located((By.ID, "user-name"))
    ).send_keys(username)

    driver.find_element(By.ID , "password").send_keys(password)
    driver.find_element(By.ID , "login-button").click()
