
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



@pytest.mark.parametrize('item', [num for num in range(43, 48)])
@pytest.mark.xfail(item=47, reason="add_to_cart() redirects to item's page instead of adding to cart")
def test_add_some_laptop_to_cart_from_category_page(category_page, browser, config, item):
    category_page.open_laptops_page()
    page = ItemPage(browser, category_page.config)
    page.add_to_cart(item)
    selected_item = page.get_item_name(item)
    assert page.should_be_alert_message() == f"Success: You have added {selected_item} to your shopping cart!\n×", \
        "No/not_correct message about added item"


## TEMPORARY TEST: test will be failed when the bug got fixed
@pytest.mark.xfail(strict=True, reason="add_to_cart() redirects to item's page instead of adding to cart")
def test_add_item47_to_cart_from_category_page_temporary_test(category_page, browser, config, item=47):
    category_page.open_laptops_page()
    page = ItemPage(browser, category_page.config)
    page.add_to_cart(item)
    selected_item = page.get_item_name(item)
    assert page.should_be_alert_message() == f"Success: You have added {selected_item} to your shopping cart!\n×", \
        "No/not_correct message about added item"




@pytest.mark.parametrize('item', [num for num in range(43, 48)])
def test_add_to_cart_from_opened_single_item_page(category_page, browser, config, item):
    category_page.open_laptops_page()
    page = ItemPage(browser, category_page.config)
    page.open_item_info_page(item)
    page.add_to_cart()
    selected_item = page.get_item_name(item)
    assert page.should_be_alert_message() == f"Success: You have added {selected_item} to your shopping cart!\n×", \
        "No/not_correct message about added item"


def test_add_random_item_to_cart_from_its_page(category_page, browser, config, item=random.randrange(43, 48)):
    category_page.open_laptops_page()
    page = ItemPage(browser, category_page.config)
    page.open_item_info_page(item)
    page.add_to_cart()
    selected_item = page.get_item_name(item)
    assert page.should_be_alert_message() == f"Success: You have added {selected_item} to your shopping cart!\n×", \
        "No/not_correct message about added item"



def test_check_cart_total_adding_item_to_cart_from_category_page(category_page, browser, config, item=random.randrange(43, 47)):
    cart = MainPage(browser, config)
    old_cart_total = cart.get_cart_total_from_cart_button()
    category_page.open_laptops_page()
    page = ItemPage(browser, category_page.config)
    item_price = page.get_item_price_from_plate(item)
    page.add_to_cart(item)
    new_cart_total = cart.get_cart_total_from_cart_button()

    old_cart_total.qty = old_cart_total.qty + 1
    old_cart_total.price = old_cart_total.price + item_price
    assert new_cart_total == old_cart_total


def test_check_cart_total_adding_item_to_cart_from_its_page(category_page, browser, config, item=random.randrange(43, 48)):
    category_page.open_laptops_page()
    page = ItemPage(browser, category_page.config)
    page.open_item_info_page(item)

    cart = MainPage(browser, config)
    old_cart_total = cart.get_cart_total_from_cart_button()
    quantity = random.randrange(10, 15)
    page.input_quantity(quantity)
    page.add_to_cart()

    new_cart_total = cart.get_cart_total_from_cart_button()

    items_total = page.get_total_item_price_and_quantity_from_item_page(quantity)
    old_cart_total.qty = old_cart_total.qty + items_total.qty
    old_cart_total.price = old_cart_total.price + items_total.price

    assert new_cart_total == old_cart_total




@pytest.mark.parametrize('item', [num for num in range(43, 47)])
def test_check_all_asserts_adding_item_to_cart(category_page, browser, config, item):
    """by using pytest-check is able to use asserts as much as needed in a same test"""
    category_page.open_laptops_page()
    page = ItemPage(browser, category_page.config)
    page.open_item_info_page(item)

    cart = MainPage(browser, config)
    old_cart_total = cart.get_cart_total_from_cart_button()
    quantity = random.randrange(3, 6)
    page.input_quantity(quantity)
    page.add_to_cart()

    new_cart_total = cart.get_cart_total_from_cart_button()

    items_total = page.get_total_item_price_and_quantity_from_item_page(quantity)
    old_cart_total.qty = old_cart_total.qty + items_total.qty
    old_cart_total.price = old_cart_total.price + items_total.price
    selected_item = page.get_item_name(item)

    ### using pytest-check as check for multiple assertion
    # check.is_true(page.should_be_alert_message() == f"Success: You have added {selected_item} to your shopping cart! ", "No/not_correct message about added item")
    check.equal(new_cart_total, old_cart_total)