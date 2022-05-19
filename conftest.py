import jsonpickle
from selenium import webdriver
# from pages.base_page import BasePage
from pages.db_helper import DbFixture
import pytest
import json
import os.path
import importlib
from selenium.webdriver.chrome.options import Options
import pymysql.cursors
from model.logger import Logger

target = None

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as fl:
            target = json.load(fl)
    return target




@pytest.fixture(scope="session")  # эта фикстура для исп другими фискстурами (zB for configure_server)
def config(request):
    return load_config(request.config.getoption("--target"))




@pytest.fixture(scope="session")
def browser(request):
    browser_param = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    if browser_param == "chrome":
        options = Options()
        if headless: options.headless = True
        driver = webdriver.Chrome(options=options)
    elif browser_param == "firefox":
        options = webdriver.FirefoxOptions()
        if headless: options.headless = True
        driver = webdriver.Firefox(options=options)
    elif browser_param == "safari":
        driver = webdriver.Safari()
    elif browser_param == "edge":
        driver = webdriver.Edge()
    else:
        raise Exception(f"{request.param} is not supported!")

    driver.implicitly_wait(10)
    request.addfinalizer(driver.close)
    # driver.get(request.config.getoption("--url"))
    return driver




@pytest.fixture(scope="session")
def db(request):  # fixture to database connection
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--headless", action="store_true", help="Run headless") ###**********
    # parser.addoption("--url", "-U", action="store", help="choose your browser")




def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])



def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())




