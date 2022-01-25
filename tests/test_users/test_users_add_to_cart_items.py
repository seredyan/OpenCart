
import pytest
from pages.login_page import LoginPage
from pages.category_page import CategoryPage
from pages.item_page import ItemPage
import generator.users
from model.users import User
import random


@pytest.fixture()
def category_page(browser, config):
    page = CategoryPage(browser, config)
    url = page.base_url
    page.open(url)
    return page





@pytest.mark.parametrize('item', [num for num in range(43, 47)])
def test_random_user_can_add_to_cart_random_item_from_category_page(db, category_page, browser, config, item):
    check_available_parameters(category_page, db)
    login_random_user(db, browser, config)
    category_page.open_laptops_page()
    page = ItemPage(browser, category_page.config)
    page.add_to_cart(item)
    assert page.should_be_success_added_to_cart_message(item), "No/not_correct message about added item"




@pytest.mark.parametrize('item', [num for num in range(43, 48)])
def test_random_user_can_add_to_cart_random_item_from_opened_single_item_page(db, category_page, browser, config, item):
    check_available_parameters(category_page, db)
    login_random_user(db, browser, config)
    category_page.open_laptops_page()
    page = ItemPage(browser, category_page.config)
    page.open_item_info_page(item)
    page.add_to_cart()
    assert page.should_be_success_added_to_cart_message(), "No/not_correct message about added item"


















def login_random_user(db, browser, config):
    page = LoginPage(browser, config)
    if not page.is_logged_in():
        old_users = db.get_users_list()
        selected_user = random.choice(old_users)
        page.login(selected_user.username, "test123")
    return



def check_available_parameters(login_page, db):
    if db.get_users_list() == []:

        firstname = generator.users.random_string("xx", 6)
        lastname = generator.users.random_string("yy", 4)
        phone = generator.users.random_digits_phone(3)
        username = generator.users.random_char_email(6)
        new_user = User(firstname=firstname, lastname=lastname, phone=phone, username=username, password='test123')
        login_page.sign_up(new_user)
        login_page.logout()