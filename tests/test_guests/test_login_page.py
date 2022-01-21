import pytest
from pages.login_page import LoginPage
from model.users import User
from generator import users


@pytest.fixture
def login_page(browser, config):
    page = LoginPage(browser, config)
    url = page.base_url
    page.open(url)
    return page

@pytest.fixture
def update_users_json():
    pass


def test_register_new_users(login_page, json_users):
    new_users = json_users
    login_page.sign_up(new_users)
    assert login_page.can_login(new_users.username, new_users.password)


### needs to be updated new users before start test!!!
def test_register_new_users_check_database(db, login_page, json_users):
    old_users = db.get_users_list()
    new_user = json_users
    login_page.sign_up(new_user)
    new_users = db.get_users_list()
    old_users.append(new_user)

    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)
