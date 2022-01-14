
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
    SHOW_ALL_IN_CATEGORIES = (By.PARTIAL_LINK_TEXT, 'Show All')
    TABLETS = (By.LINK_TEXT, "Tablets")
    COMPONENTS = (By.LINK_TEXT, "Components")
    PHONES = (By.PARTIAL_LINK_TEXT, "Phones")
    CAMERAS = (By.LINK_TEXT, "Cameras")
    MP3_PLAYERS = (By.PARTIAL_LINK_TEXT, "MP3")


class ItemPageLocators:

    ADD_TO_CART_FROM_ITEM_PAGE = (By.CSS_SELECTOR, "#button-cart")
    APPENDED_PART_TO_ITEM_PAGE = (By.CSS_SELECTOR, "h4 a")
    ITEM_PLATES = (By.CSS_SELECTOR, "div.product-thumb")
    ITEM_NAME_ON_ITEM_PAGE = (By.CSS_SELECTOR, "#content div.col-sm-4 h1")
    MAC_DESKTOP = (By.PARTIAL_LINK_TEXT, 'Mac')
    SUCCESS_ADD_ITEM_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")
    ITEM_PRICE_ON_ITEM_PAGE = (By.CSS_SELECTOR, "#content div.col-sm-4 h2")
    INPUT_QUANTITY = (By.CSS_SELECTOR, "#input-quantity")




class LoginPageLocators:
    pass

class MainPageLocators:
    ADD_TO_CART_FROM_OPTIONS = (By.CSS_SELECTOR, "button[onclick^='cart.add']")
    BUTTON_CART_TOTAL = (By.CSS_SELECTOR, "#cart-total")



