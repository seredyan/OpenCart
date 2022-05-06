
import pytest

from pages.category_page import CategoryPage
from pages.item_page import ItemPage
from pages.cart_page import CartPage


@pytest.fixture()
def category_page(browser, config):
    page = CategoryPage(browser, config)
    url = page.base_url
    page.open(url)
    return page


def test_cart_page_after_adding_item(browser, config, category_page, item=40):
    page = ItemPage(browser, config)
    page.add_to_cart(item)
    selected_item = page.get_item_name(item)
    cart_page = CartPage(browser, config)
    cart_page.open_cart_page()
    a = cart_page.get_item_name_in_cart()

    print(a)

