
from .locators import CartPageLocators
from .base_page import BasePage
import time





class CartPage(BasePage):

    def open_cart(self):
        self.browser.find_element(*CartPageLocators.CART_LINK).click()



