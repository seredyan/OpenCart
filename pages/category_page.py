
from .base_page import BasePage
from .locators import CategoryPageLocators, ItemPageLocators

class CategoryPage(BasePage):

    def open_desktops_page(self):
        self.browser.find_element(*CategoryPageLocators.DESKTOPS).click()
        self.open_all_in_categories()

    def open_laptops_page(self):
        self.browser.find_element(*CategoryPageLocators.LAPTOPS).click()
        self.open_all_in_categories()









    """auxiliary methods """

    def open_all_in_categories(self):
        self.browser.find_element(*CategoryPageLocators.SHOW_ALL_IN_CATEGORIES).click()