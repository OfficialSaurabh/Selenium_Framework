from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages.home.login_page import LoginPage
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.login("test07@mailinator.com", "Test@123")
        time.sleep(3)
        result = self.lp.verify_login_successful()
        assert result == True

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.lp.login("test07@mailinator.com", "Test@12")
        result = self.lp.verify_login_failed()
        assert result == True
        # self.driver.quit()
