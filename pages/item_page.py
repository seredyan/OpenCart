import random
import time
import re
from pages.base_page import BasePage
from .locators import ItemPageLocators, MainPageLocators
from model.cart import Cart



class ItemPage(BasePage):

    def add_to_cart(self, item_id=None):  ## there is designed to use 2 different locators for add_to_cart button
        if not item_id == None:
            item = self.select_item(item_id)
            item.find_element(*MainPageLocators.ADD_TO_CART_FROM_OPTIONS).click() ## add to cart item from item's group
        else:
            self.browser.find_element(*ItemPageLocators.ADD_TO_CART_FROM_ITEM_PAGE).click() ## add to cart item from single item's page
        time.sleep(2)  # it's needed because of cart_total takes time to be changed



    """auxiliary methods """


    def select_item(self, item_id):  # item_id must be assigned by testers
        items = self.browser.find_elements(*ItemPageLocators.ITEM_PLATES)  # find of group of item's plates
        for item in items:
            if int((item.find_element(*ItemPageLocators.APPENDED_PART_TO_ITEM_PAGE).get_attribute('href')).split("id=", 1)[1]) == item_id:
                selected_item = item
                return selected_item
        return



    def select_desktop(self):
        self.browser.find_element(*ItemPageLocators.MAC_DESKTOP).click()



    def open_item_info_page(self, item_id):
        item = self.select_item(item_id)
        item.find_element(*ItemPageLocators.APPENDED_PART_TO_ITEM_PAGE).click()
        time.sleep(1)


    def success_added_to_cart_message_present(self, item_id=None):
        message = self.browser.find_element(*ItemPageLocators.SUCCESS_ADD_ITEM_MESSAGE).text
        product_name = self.get_item_name(item_id)
        return "Success" and product_name and "shopping cart" in message


    def get_item_name(self, item_id=None):
        if "category" in self.browser.current_url or self.browser.current_url.endswith("/home"):
            item = self.select_item(item_id)
            return item.find_element(*ItemPageLocators.APPENDED_PART_TO_ITEM_PAGE).text
        else:
            return self.browser.find_element(*ItemPageLocators.ITEM_NAME_ON_ITEM_PAGE).text




    def get_total_item_price_and_quantity_from_item_page(self, qty):
        info_price = self.browser.find_element(*ItemPageLocators.ITEM_PRICE_ON_ITEM_PAGE).text
        total = self.manage_price_text(info_price)
        return Cart(qty=qty, price=total*qty)


    def input_quantity(self, qty):
        """input_quantity by adding to cart"""
        return self.change_field_value(*ItemPageLocators.INPUT_QUANTITY, qty)


    def get_item_price_from_plate(self, item_id=None):
        """provides clear price"""
        info_price = self.ccollect_all_info_price_from_plate(item_id)
        get_total = re.search("\d+\,*?\d+\.*?\d+", info_price).group(0)
        total = float(get_total.replace(',', ''))
        return total


    def ccollect_all_info_price_from_plate(self, item_id=None):
        """reads info about full price (include Tax) from the item's plate on the category_page"""
        item = self.select_item(item_id)
        return item.find_element(*ItemPageLocators.APPENDED_PART_ITEM_PRICE).text



