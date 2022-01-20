import pytest
from pages.login_page import LoginPage


@pytest.fixture
def login_page(browser, config):
    page = LoginPage(browser, config)
    url = page.base_url
    page.open(url)
    return page


def test_register_new_users(login_page, json_users):
    new_users = json_users
    login_page.sign_up(new_users)
    assert login_page.can_login(new_users)

