
from .base_page import BasePage
from .locators import MainPageLocators
import re
from model.cart import Cart


class MainPage(BasePage):




    def get_cart_total_from_cart_button(self):
        self.browser.implicitly_wait(5)
        all_info = self.browser.find_element(*MainPageLocators.BUTTON_CART_TOTAL).text
        cart_info = self.process_info_from_cart(all_info)
        return cart_info


    def process_info_from_cart(self, text):  # get text from cart
        item = int(re.search("\d+", text).group())
        total = self.manage_text(text)
        return Cart(qty=item, price=total)