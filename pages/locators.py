
from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, " .dropdown .caret")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, " .dropdown .caret_inv")  ## for test NoSuchElementException
    DISPLAYED_BASKET = (By.ID, "cart-total")


class CartPageLocators:
    CART_LINK = (By.LINK_TEXT, "Shopping Cart")
    CART_CHECKOUT = (By.CSS_SELECTOR, "a.btn-primary")  ## ?????


class CategoryPageLocators:
    DESKTOPS = (By.LINK_TEXT, "Desktops")
    LAPTOPS = (By.PARTIAL_LINK_TEXT, "Laptops")
    TABLETS = (By.LINK_TEXT, "Tablets")

class ItemPageLocators:
    ADD_TO_CART = (By.CSS_SELECTOR, "button[onclick^='cart.add']")
    MAC = (By.PARTIAL_LINK_TEXT, 'Mac')
    ALL_LAPTOPS = (By.PARTIAL_LINK_TEXT, 'Show All Laptops')

class LoginPageLocators:
    pass

class MainPageLocators:
    pass


