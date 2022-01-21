
from pages.login_page import LoginPage
from model.users import User
import random
import generator.users


def test_edit_lastname(db, browser, config):
    check_available_parameters(db, browser)
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



def check_available_parameters(db, browser):
    if db.get_users_list() == []:

        firstname = generator.users.random_string("xx", 6)
        lastname = generator.users.random_string("yy", 4)
        phone = generator.users.random_digits_phone(3)
        username = generator.users.random_char_email(6)
        new_user = User(firstname=firstname, lastname=lastname, phone=phone, username=username, password='test123')
        browser.users_helper.sign_up(new_user)