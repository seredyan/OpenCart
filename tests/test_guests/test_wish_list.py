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


def test_add_item_to_wishlist_from_category_page(category_page, browser, config, item=43):
    page = ItemPage(browser, category_page.config)
    page.add_to_wish_list(item)
    assert page.should_be_warning_message()
