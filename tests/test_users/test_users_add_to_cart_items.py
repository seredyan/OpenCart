import time

import pytest
from pages.login_page import LoginPage
from pages.category_page import CategoryPage
from pages.item_page import ItemPage
from model.cart import Cart
import random


@pytest.fixture(scope="function")
def user_login(db, browser, config, category_page):
    login_page = LoginPage(browser, config)
    login_page.check_available_users(db)
    selected_user = random.choice(db.get_users_list())
    login_page.login(selected_user.username, "test123")
    login_page.ensure_login(selected_user.username, "test123")
    return selected_user


@pytest.fixture
def category_page(browser, config):
    page = CategoryPage(browser, config)
    url = page.base_url
    page.open(url)
    return page

@pytest.fixture(scope="function")
def items_in_cart(db):
    cart = db.get_items_in_cart_list()
    return cart


@pytest.mark.parametrize('item', [num for num in range(43, 47)])
def test_random_user_can_add_to_cart_random_item_from_category_page(db, user_login, category_page, browser, config, item):
    category_page.open_laptops_page()
    page = ItemPage(browser, category_page.config)
    page.add_to_cart(item)
    selected_item = page.get_item_name(item)
    assert page.should_be_alert_message() == f"Success: You have added {selected_item} to your shopping cart!\n×", \
        "No/not_correct message about added item"




@pytest.mark.parametrize('item', [num for num in range(43, 48)])
def test_random_user_can_add_to_cart_random_item_from_opened_single_item_page(db, category_page, user_login, browser, config, item):
    category_page.open_laptops_page()
    page = ItemPage(browser, category_page.config)
    page.open_item_info_page(item)
    page.add_to_cart()
    selected_item = page.get_item_name(item)
    assert page.should_be_alert_message() == f"Success: You have added {selected_item} to your shopping cart!\n×", \
        "No/not_correct message about added item"





def test_check_cart_after_user_added_to_cart_some_item(db, items_in_cart, user_login, category_page, browser, config, item=45):

    category_page.open_laptops_page()
    page = ItemPage(browser, category_page.config)
    page.add_to_cart(item)
    new_cart = db.get_items_in_cart_list()
    used_cart = Cart(customer=int(user_login.id), product=item, qty=1)
    quantity = page.get_qty(used_cart, items_in_cart, new_cart)

    assert items_in_cart == new_cart
    assert quantity[0] == quantity[1]









