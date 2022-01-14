
from .base_page import BasePage
from .locators import MainPageLocators
import re
from model.cart import Cart


class MainPage(BasePage):




    def get_cart_total_from_cart_button(self):
        all_info = self.browser.find_element(*MainPageLocators.BUTTON_CART_TOTAL).text
        cart_info = self.process_info_from_cart(all_info)
        return cart_info





    def process_info_from_cart(self, text):  # get text from cart

        all_numbers = "\d+\,*?\d+"
        item = int(re.search("\d+", text).group())
        all_amount = re.findall(all_numbers, text)
        total = int(all_amount[0].replace(',', ''))

        return Cart(qty=item, price=total)