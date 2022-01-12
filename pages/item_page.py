import random
import time

from pages.base_page import BasePage
from .locators import ItemPageLocators, MainPageLocators



class ItemPage(BasePage):


    def add_item_into_cart(self, item_id):
        item = self.select_item(item_id)
        self.add_to_cart(item)

    def select_desktop(self):
        self.browser.find_element(*ItemPageLocators.MAC_DESKTOP).click()






    """auxiliary methods """

    def add_to_cart(self, item):
        item.find_element(*MainPageLocators.ADD_TO_CART_FROM_OPTIONS).click()



    def select_item(self, item_id):
        items = self.browser.find_elements(*ItemPageLocators.ITEM_PLATES)
        for item in items:
            if int((item.find_element(*ItemPageLocators.ITEM_PARTIAL_LINKS).get_attribute('href')).split("id=", 1)[1]) == item_id:
                selected_item = item
                return selected_item
        return

