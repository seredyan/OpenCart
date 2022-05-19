
import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from model.logger import Logger
from pages.locators import BasePageLocators



class BasePage:

    def __init__(self, browser, config, timeout=10):  # run browser

        self.browser = browser
        self.config = config
        self.base_url = config['web']['baseUrl']
        browser.implicitly_wait(timeout)
        Logger.add_log(browser)




    def change_field_value(self, selector, field_name, text):
        if text is not None:
            self.browser.find_element(selector, field_name).click()
            self.browser.find_element(selector, field_name).clear()
            self.browser.find_element(selector, field_name).send_keys(text)



    def go_to_basket(self):
        self.browser.find_element(*BasePageLocators.DISPLAYED_BASKET).click()

    def go_to_login_page(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()


    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True




    def is_not_element_present(self, how, what, timeout=3):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False


    def is_disappeared(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True


    def manage_price_text(self, info_price):
        """produces a clean digit of total from the received text """
        price = info_price.split("$", 1)[1]
        total = float(price.replace(',', ''))
        return total


    def open(self, url):
        wd = self.browser
        wd.get(url)



    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not present"




    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not present," \
                                                                     " probably unauthorised user"

    # def is_valid(self):
    #     try:
    #         self.browser.current_url
    #         return True
    #     except:
    #         return False
    #
    # def destroy(self):
    #     self.browser.quit()