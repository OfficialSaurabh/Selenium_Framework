from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages.home.login_page import LoginPage
import unittest

class LoginTest(unittest.TestCase):
    def test_valid_login(self):
        baseURL = "https://www.letskodeit.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        lp = LoginPage(driver)
        lp.login("test07@mailinator.com", "Test@123")


        user_icon = driver.find_element(By.XPATH, "//button[@id='dropdownMenu1']//img")
        if user_icon is not None:
            print("Login Successful")
        else:
            print("Login Failed")

        driver.quit()







