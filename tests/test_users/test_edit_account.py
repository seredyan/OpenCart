
from pages.login_page import LoginPage
from model.users import User
import random
import generator.users


def test_edit_users_lastname(db, browser, config):
    check_available_parameters(db, browser, config)
    old_users = db.get_users_list()
    selected_user = random.choice(old_users)

    index = old_users.index(selected_user)
    page = LoginPage(browser, config)
    url = page.base_url
    page.open(url)

    modified_user = User(lastname="NEW_LASTNAME_77777")
    page.edit_account(selected_user.username, modified_user, password="test123")
    new_users = db.get_users_list()
    old_users[index].lastname = modified_user.lastname

    assert old_users == new_users




def test_edit_users_firstname(db, browser, config):
    check_available_parameters(db, browser, config)
    old_users = db.get_users_list()
    selected_user = random.choice(old_users)

    index = old_users.index(selected_user)
    page = LoginPage(browser, config)
    url = page.base_url
    page.open(url)

    modified_user = User(firstname="NEW_FIRSTNAME_EEEE")
    page.edit_account(selected_user.username, modified_user, password="test123")
    new_users = db.get_users_list()
    old_users[index].firstname = modified_user.firstname

    assert old_users == new_users


def test_edit_users_phone_number(db, browser, config):
    check_available_parameters(db, browser, config)
    old_users = db.get_users_list()
    selected_user = random.choice(old_users)

    index = old_users.index(selected_user)
    page = LoginPage(browser, config)
    url = page.base_url
    page.open(url)

    modified_user = User(phone="777777")
    page.edit_account(selected_user.username, modified_user, password="test123")
    new_users = db.get_users_list()
    old_users[index].phone = modified_user.phone

    assert old_users == new_users



def test_edit_users_username_account(db, browser, config):
    check_available_parameters(db, browser, config)
    old_users = db.get_users_list()
    selected_user = random.choice(old_users)

    index = old_users.index(selected_user)
    page = LoginPage(browser, config)
    url = page.base_url
    page.open(url)

    edited_username = generator.users.random_char_email(6)
    modified_user = User(username=edited_username)
    page.edit_account(selected_user.username, modified_user, password="test123")
    new_users = db.get_users_list()
    old_users[index].username = modified_user.username

    assert old_users == new_users




def check_available_parameters(db, browser, config):
    if db.get_users_list() == []:

        firstname = generator.users.random_string("xx", 6)
        lastname = generator.users.random_string("yy", 4)
        phone = generator.users.random_digits_phone(3)
        username = generator.users.random_char_email(6)
        new_user = User(firstname=firstname, lastname=lastname, phone=phone, username=username, password='test123')
        page = LoginPage(browser, config)
        url = page.base_url
        page.open(url)
        page.sign_up(new_user)
        page.logout()