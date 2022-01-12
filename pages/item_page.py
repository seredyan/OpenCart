from pages.base_page import BasePage
from .locators import ItemPageLocators



class ItemPage(BasePage):



    def add_item_into_cart(self):
        self.select_item()
        self.add_to_cart()

    def select_desktop(self):
        self.browser.find_element(*ItemPageLocators.MAC_DESKTOP).click()


    def select_laptops_page(self):
        self.browser.find_element(*ItemPageLocators.ALL_LAPTOPS).click()




    """auxiliary methods """

    def add_to_cart(self):
        self.browser.find_element(*ItemPageLocators.ADD_TO_CART).click()


    def select_item(self):
        pass
