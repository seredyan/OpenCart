
from .locators import CartPageLocators
from .base_page import BasePage
from model.product import Product
import time





class CartPage(BasePage):

    def open_cart_page(self):
        self.browser.find_element(*CartPageLocators.CART_LINK).click()


    def get_item_info_in_cart(self):

        row = self.browser.find_element(*CartPageLocators.ITEM_NAME)
        id = int((row.get_attribute('href')).split("id=", 1)[1])
        name = row.text
        qty = self.browser.find_element(*CartPageLocators.ITEM_QTY)
        item = Product(id=id, name=name, qty=qty)
        return item








