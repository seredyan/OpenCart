
from .base_page import BasePage
from .locators import CategoryPageLocators, ItemPageLocators

class CategoryPage(BasePage):

    def open_desktops_page(self):
        self.browser.find_element(*CategoryPageLocators.DESKTOPS).click()

    def open_laptop_page(self):
        self.browser.find_element(*CategoryPageLocators.LAPTOPS).click()
        self.browser.find_element(*CategoryPageLocators.SHOW_ALL_IN_CATEGORIES).click()
