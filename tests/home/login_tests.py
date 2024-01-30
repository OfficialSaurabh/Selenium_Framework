from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.login("test07@mailinator.com", "Test@123")
        time.sleep(3)
        # Verify title
        result1 = self.lp.verify_title()
        self.ts.mark(result1, "Title Verification")
        result2 = self.lp.verify_login_successful()
        self.ts.markFinal("test_valid_login", result2, "Login Successful")

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.lp.login("test07@mailinator.com", "Test@12")
        result = self.lp.verify_login_failed()
        assert result == True
        # self.driver.quit()
