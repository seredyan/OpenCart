from operator import attrgetter

from model.cart import Cart
import pytest
from pages.login_page import LoginPage
from pages.category_page import CategoryPage
from pages.item_page import ItemPage
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
def old_wish_list(db):
    wish_list = db.get_items_in_wish_list()
    return wish_list


def test_user_adds_item_to_wishlist_from_category_page(db, old_wish_list, category_page, user_login, browser, config, item=random.randrange(43, 48)):

    category_page.open_laptops_page()
    page = ItemPage(browser, category_page.config)
    page.add_to_wish_list(item)
    selected_item = page.get_item_name(item)

    used_wish_list = Cart(customer=int(user_login.id), product=item)
    old_wish_list.append(used_wish_list)
    new_wish_list = db.get_items_in_wish_list()

    assert sorted(old_wish_list, key=attrgetter('customer', 'product')) == new_wish_list
    print("old: ", old_wish_list)
    print("new: ", new_wish_list)
    assert page.should_be_alert_message() == f"Success: You have added {selected_item} to your wish list!\n×", \
        "There is no warning message or wrong message about the wishlist"
