import time

import pytest
from pages.category_page import CategoryPage
from pages.item_page import ItemPage
import random


@pytest.fixture()
def category_page(browser, config):
    page = CategoryPage(browser, config)
    url = page.base_url
    page.open(url)
    return page


def test_guest_adds_item_to_wishlist_from_category_page(category_page, browser, config, item=43):
    page = ItemPage(browser, category_page.config)
    page.add_to_wish_list(item)

    assert page.should_be_wishlist_warning_message(item), "There is no warning message about the wishlist"
    assert page.go_to_login_from_alert_message(), "Unable to go to login page from wishlist alert message"


def test_guest_adds_item_to_wishlist_from_category_page_and_go_to_registration(category_page, browser, config, item=40):
    page = ItemPage(browser, category_page.config)
    page.add_to_wish_list(item)

    assert page.should_be_wishlist_warning_message(item), "There is no warning message about the wishlist"
    assert page.go_to_registration_from_alert_message(), "Unable to go to regiatration page from wishlist alert message"