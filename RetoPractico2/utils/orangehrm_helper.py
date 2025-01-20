# utils/orangehrm_helper.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrangeHRMHelper:

    def __init__(self, browser):
        self.browser = browser

    def open_orangehrm(self):
        self.browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def login(self, username, password):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.NAME, "username")))
        self.browser.find_element(By.NAME, "username").send_keys(username)
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.NAME, "password")))
        self.browser.find_element(By.NAME, "password").send_keys(password)
        self.browser.find_element(By.XPATH, "//button[@type='submit']").click()
        return self.browser.current_url
