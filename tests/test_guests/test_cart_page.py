
import pytest

from model.product import Product
from pages.category_page import CategoryPage
from pages.item_page import ItemPage
from pages.cart_page import CartPage


@pytest.fixture()
def category_page(browser, config):
    page = CategoryPage(browser, config)
    url = page.base_url
    page.open(url)
    return page


def test_cart_page_after_adding_single_item(browser, config, category_page, item=40):
    page = ItemPage(browser, config)
    page.add_to_cart(item)
    selected_item = page.get_item_name(item)
    cart_page = CartPage(browser, config)
    cart_page.open_cart_page()
    added_item = Product(name=selected_item, id=item)
    item_in_cart = cart_page.get_item_info_in_cart()

    assert added_item == item_in_cart

def test111(browser, config, category_page):
    page = ItemPage(browser, config)
    return page