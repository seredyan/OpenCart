
from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, " .dropdown .caret")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, " .dropdown .caret_inv")  ## for test NoSuchElementException
    DISPLAYED_BASKET = (By.ID, "cart-total")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")


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
    APPENDED_PART_ITEM_PRICE = (By.CSS_SELECTOR, ".price")
    ITEM_PLATES = (By.CSS_SELECTOR, "div.product-thumb")
    ITEM_NAME_ON_ITEM_PAGE = (By.CSS_SELECTOR, "#content div.col-sm-4 h1")
    MAC_DESKTOP = (By.PARTIAL_LINK_TEXT, 'Mac')
    ITEM_PRICE_ON_ITEM_PAGE = (By.CSS_SELECTOR, "#content div.col-sm-4 h2")
    INPUT_QUANTITY = (By.CSS_SELECTOR, "#input-quantity")




class LoginPageLocators:
    CHECK_BOX_PRIVACY_POLICY_AGREE = (By.NAME, "agree")
    CONTINUE_TO_REGISTER = (By.CSS_SELECTOR, "input[value='Continue']")
    CONTINUE_TO_FINISH_REGISTRATION = (By.CSS_SELECTOR, ".buttons .btn-primary")
    GO_TO_REGISTER = (By.LINK_TEXT, "Register")
    GO_TO_LOGIN = (By.LINK_TEXT, "Login")
    LOGIN = (By.CSS_SELECTOR, "input[value='Login']")
    LOGOUT = (By.LINK_TEXT, "Logout")
    MY_ACCOUNT = (By.CSS_SELECTOR, ".list-inline .dropdown a.dropdown-toggle")
    REGISTER_FIRST_NAME = (By.CSS_SELECTOR, "#input-firstname")
    REGISTER_LAST_NAME = (By.CSS_SELECTOR, "#input-lastname")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#input-email")
    REGISTER_PHONE = (By.CSS_SELECTOR, "#input-telephone")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#input-confirm")
    # EDIT_ACCOUNT = (By.CSS_SELECTOR, "a.list-group-item:nth-child(2)")
    EDIT_ACCOUNT = (By.LINK_TEXT, "Edit Account")


class MainPageLocators:
    ADD_TO_CART_FROM_OPTIONS = (By.CSS_SELECTOR, "button[onclick^='cart.add']")
    BUTTON_CART_TOTAL = (By.CSS_SELECTOR, "#cart-total")



