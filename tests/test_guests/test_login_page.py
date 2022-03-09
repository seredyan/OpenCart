import os
import random

import pytest
from pages.login_page import LoginPage
from model.users import User



@pytest.fixture
def login_page(browser, config):
    page = LoginPage(browser, config)
    url = page.base_url
    page.open(url)
    return page




def test_register_new_users(db, login_page, json_users):
    new_users = json_users
    login_page.sign_up(new_users)
    assert login_page.can_login(new_users.username, new_users.password)



### needs to be updated new users before start test!!!
def test_register_new_users_check_database(db, login_page, data_users):
    old_users = db.get_users_list()
    new_user = data_users
    login_page.sign_up(new_user)
    new_users = db.get_users_list()
    old_users.append(new_user)
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)


fields = [
User(firstname=None, lastname="Dylan", username="user5@localhost.com", password="test123", phone='777'),
User(firstname="Bob", lastname=None, username="user5@localhost.com", password="test123", phone='777'),
User(firstname="Bob", lastname="Dylan", username=None, password="test123", phone='777'),
User(firstname="Bob", lastname="Dylan", username="user5@localhost.com", password=None, phone='777'),
User(firstname="Bob", lastname="Dylan", username="user5@localhost.com", password="test123", phone=None)
]
@pytest.mark.parametrize('field', fields)
def test_attempt_register_new_user_with_missing_field(db, login_page, field):
    old_users = db.get_users_list()
    login_page.sign_up(field)
    new_users = db.get_users_list()
    assert login_page.should_be_alert_wrong_or_missing_fields()
    assert old_users == new_users


def test_register_new_users_with_wrong_type_email(db, login_page, data_users):
    old_users = db.get_users_list()
    new_user = data_users
    new_user.username = "wrongemaillocalhost@dd"
    login_page.sign_up(new_user)
    new_users = db.get_users_list()
    assert login_page.should_be_alert_wrong_or_missing_fields()
    assert old_users == new_users


def test_register_new_users_with_wrong_type_password(db, login_page, data_users):
    old_users = db.get_users_list()
    new_user = data_users
    new_user.password = random.randrange(1, 4)
    login_page.sign_up(new_user)
    new_users = db.get_users_list()
    assert login_page.should_be_alert_wrong_or_missing_fields()
    assert old_users == new_users


