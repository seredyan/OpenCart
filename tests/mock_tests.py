
import pytest
from pages.cart_page import CartPage


@pytest.fixture()
def cart_page(browser, config):
    page = CartPage(browser, config)
    url = page.base_url
    page.open(url)
    return page


def mock_test1(cart_page):
    cart_page.open_cart()