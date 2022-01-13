import random
import time

from pages.base_page import BasePage
from .locators import ItemPageLocators, MainPageLocators



class ItemPage(BasePage):

    def add_to_cart(self, item_id=None):
        if not item_id == None:
            item = self.select_item(item_id)
            item.find_element(*MainPageLocators.ADD_TO_CART_FROM_OPTIONS).click()
        else:
            self.browser.find_element(*ItemPageLocators.ADD_TO_CART_FROM_ITEM_PAGE).click()



    """auxiliary methods """


    def select_item(self, item_id):
        items = self.browser.find_elements(*ItemPageLocators.ITEM_PLATES)
        for item in items:
            if int((item.find_element(*ItemPageLocators.APPENDED_PART_TO_ITEM_PAGE).get_attribute('href')).split("id=", 1)[1]) == item_id:
                selected_item = item
                return selected_item
        return



    def select_desktop(self):
        self.browser.find_element(*ItemPageLocators.MAC_DESKTOP).click()


    def open_item_info_page(self):
        pass