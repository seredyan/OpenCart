
from .locators import CartPageLocators
from .base_page import BasePage
from model.product import Product
import time





class CartPage(BasePage):

    def open_cart_page(self):
        self.browser.find_element(*CartPageLocators.CART_LINK).click()


    def get_item_name_in_cart(self):

        self.item_cashe = []
        row = self.browser.find_element(*CartPageLocators.ITEM_NAME).text

        # id = int((row.get_attribute('href')).split("id=", 1)[1])

        # name = row.text
        return row
            # self.item_cashe.append(Product(id=id, name=name))








