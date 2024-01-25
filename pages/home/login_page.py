from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locator
    _login_link = "//a[@href='/login']"
    _email_field = "email"
    _password_field = "login-password"
    _login_button = "login"

    # def get_login_link(self):
    #     return self.driver.find_element(By.XPATH, self._login_link)
    #
    # def get_email_filed(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    #
    # def get_password_field(self):
    #     return self.driver.find_element(By.ID, self._password_field)
    #
    # def get_login_button(self):
    #     return self.driver.find_element(By.ID, self._login_button)

    def click_login_link(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def enter_email(self, email):
        self.sendKeys(email, self._email_field)

    def enter_password(self, password):
        self.sendKeys(password, self._password_field)

    def click_login_button(self):
        self.elementClick(self._login_button)

    def login(self, email, password):
        self.click_login_link()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
