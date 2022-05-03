
import random

import pytest
from pages.item_page import ItemPage
from pages.category_page import CategoryPage
from pages.main_page import MainPage
import pytest_check as check


@pytest.fixture()
def category_page(browser, config):
    page = CategoryPage(browser, config)
    url = page.base_url
    page.open(url)
    return page

@pytest.fixture()
def item_page(category_page, browser, config):
    category_page.open_laptops_page()
    item_page = ItemPage(browser, category_page.config)
    return item_page


def test_check_item_title_page(item_page, browser, config, item=46):
    item_page.open_item_info_page(item)
    selected_item = item_page.get_item_name(item)

    assert item_page.get_page_title() == selected_item


