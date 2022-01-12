from pages.base_page import BasePage
from .locators import ItemPageLocators



class ItemPage(BasePage):

    def add_to_cart(self):
        self.browser.find_element(*ItemPageLocators.ADD_TO_CART).click()


    def select_desktop(self):
        self.browser.find_element(*ItemPageLocators.MAC).click()


    def select_laptops_page(self):
        self.browser.find_element(*ItemPageLocators.ALL_LAPTOPS).click()


