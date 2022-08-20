"""
Setup test configurations
"""
import os
import time

import allure
import pytest
from dotenv import load_dotenv
from selene import have, command
from selene.support.shared import browser
from selenium import webdriver

DEFAULT_BROWSER='chrome'
DEFAULT_REMOTE_DRIVER = 'selenoid.autotests.cloud'
DEFAULT_BROWSER_VERSION = '100.0'
BASE_BROWSER_TIMEOUT=10
SELENE_TIMEOUT=3


@pytest.fixture(scope='session', autouse=True)
def load_env():
    """
    Load .env
    """
    load_dotenv()


def pytest_addoption(parser):
    """
    Parser option
    """
    parser.addoption(
        '--remote_driver',
        default=DEFAULT_REMOTE_DRIVER
    )


@pytest.fixture(scope='function', autouse=True)
@allure.step('Set up browser url, browser type')
def init(request):
    remote_driver = request.config.getoption('--remote_driver')
    remote_driver = remote_driver if remote_driver != "" else DEFAULT_REMOTE_DRIVER
    capabilities = {
        "browserName": DEFAULT_BROWSER,
        "browserVersion": DEFAULT_BROWSER_VERSION,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    selenoid = f"https://{os.getenv('LOGIN')}:{os.getenv('PASSWORD')}@{remote_driver}/wd/hub"
    browser.config.driver = webdriver.Remote(
        command_executor=selenoid,
        desired_capabilities=capabilities)

    browser.config.browser_name = os.getenv('selene.browser_name', DEFAULT_BROWSER)
    browser.config.hold_browser_open = (
            os.getenv('selene.hold_browser_open', 'false').lower() == 'true'
    )
    browser.config.timeout = float(os.getenv('selene.timeout', SELENE_TIMEOUT))


@allure.step('Open page: {path}')
def open_page(path: str):
    browser.open(path)
    time.sleep(1)
    (
        browser.all('[id^=google_ads][id$=container__],[id$=Advertisement]')
        .with_(timeout=BASE_BROWSER_TIMEOUT)
        .should(have.size_greater_than_or_equal(3))
        .perform(command.js.remove)
    )
