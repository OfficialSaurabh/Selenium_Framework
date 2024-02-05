import utilities.custom_logger as cl
from base.basepage import BasePage
import logging
import time


class RegisterCoursesPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _all_course = "//a[@href='/courses']"
    _search_box = "//input[@id='search']"
    _search_btn = "//button[@type='submit']//i"
    _course = "//div[@id='course-list']//h4[contains(text(),'{}')]"
    _all_coursers = "course-list"
    _enroll_button = "//button[contains(@class,'btn-enroll')]"
    _cc_num = "//input[@aria-label='Credit or debit card number']"
    _cc_exp = "//input[@name='exp-date']"
    _cc_cvc = "//input[@name='cvc']"
    _ccnum_iframe_xpath = "//iframe[@title='Secure card number input frame']"
    _ccexp_iframe_xpath ="//iframe[@title='Secure expiration date input frame']"
    _cccvc_iframe_xpath ="//iframe[@title='Secure CVC input frame']"
    _submit_enroll = "//button[contains(@class,'sp-buy')]"
    _enroll_error_message = "//div[contains(@class,'has-error')]"

    def clickAllCourse(self):
        time.sleep(2)
        self.elementClick(self._all_course, locatorType="xpath")

    def enterCourseName(self, name):
        self.sendKeys(name, locator=self._search_box, locatorType="xpath")
        self.elementClick(self._search_btn, locatorType="xpath")


    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locator=self._course.format(fullCourseName), locatorType="xpath")

    def clickOnEnrollButton(self):
        self.elementClick(locator=self._enroll_button, locatorType="xpath")

    def enterCardNum(self, num):
        # self.SwitchFrameByIndex(self._cc_num, locatorType="xpath")
        time.sleep(3)
        self.switchToFrame(xpath=self._ccnum_iframe_xpath)
        time.sleep(3)
        self.sendKeys(num, locator=self._cc_num, locatorType="xpath")
        time.sleep(3)
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        self.switchToFrame(xpath=self._ccexp_iframe_xpath)
        self.sendKeys(exp, locator=self._cc_exp, locatorType="xpath")
        self.switchToDefaultContent()


    def enterCardCVV(self, cvv):
        self.switchToFrame(xpath=self._cccvc_iframe_xpath)
        self.sendKeys(cvv, locator=self._cc_cvc, locatorType="xpath")
        self.switchToDefaultContent()


    def clickEnrollSubmitButton(self):
        self.elementClick(locator=self._submit_enroll, locatorType="xpath")

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)

    def enrollCourse(self, num="", exp="", cvv=""):
        self.clickOnEnrollButton()
        self.webScroll(direction="down")
        self.enterCreditCardInformation(num, exp, cvv)
        self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        messageElement = self.waitForElement(self._enroll_error_message, locatorType="xpath")
        result = self.isElementDisplayed(element=messageElement)
        return result
