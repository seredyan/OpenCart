import pytest

from pages.login_page import LoginPage
from model.users import User
import random
import generator.users

@pytest.fixture
def login_page(browser, config):
    page = LoginPage(browser, config)
    url = page.base_url
    page.open(url)
    return page


@pytest.fixture(scope="function")
def get_selected_user(db, browser, config, login_page):
    login_page.check_available_users(db)
    global old_users
    old_users = db.get_users_list()
    selected_user = random.choice(old_users)
    return selected_user



def test_edit_users_lastname(login_page, get_selected_user, db, browser, config):
    index = old_users.index(get_selected_user)
    modified_user = User(lastname="NEW_LASTNAME_77777")

    login_page.edit_account(get_selected_user.username, modified_user, password="test123")
    new_users = db.get_users_list()
    old_users[index].lastname = modified_user.lastname

    assert old_users == new_users




def test_edit_users_firstname(login_page, get_selected_user, db, browser, config):
    index = old_users.index(get_selected_user)
    modified_user = User(firstname="NEW_FIRSTNAME_EEEE")

    login_page.edit_account(get_selected_user.username, modified_user, password="test123")
    new_users = db.get_users_list()
    old_users[index].firstname = modified_user.firstname

    assert old_users == new_users


def test_edit_users_phone_number(login_page, get_selected_user, db, browser, config):
    index = old_users.index(get_selected_user)
    modified_user = User(phone="777777")

    login_page.edit_account(get_selected_user.username, modified_user, password="test123")
    new_users = db.get_users_list()
    old_users[index].phone = modified_user.phone

    assert old_users == new_users



def test_edit_users_username_account(login_page, get_selected_user, db, browser, config):
    index = old_users.index(get_selected_user)
    edited_username = generator.users.random_char_email(6)
    modified_user = User(username=edited_username)

    login_page.edit_account(get_selected_user.username, modified_user, password="test123")
    new_users = db.get_users_list()
    old_users[index].username = modified_user.username

    assert old_users == new_users


