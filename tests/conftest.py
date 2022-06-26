import pytest
from selene.support.shared import browser

url = 'https://demoqa.com/automation-practice-form'
name = 'chrome'
width = '1360'
height = '768'


@pytest.fixture(scope='session', autouse=True)
def config():
    browser.config.base_url = url
    browser.config.browser_name=name
    browser.config.window_width = width
    browser.config.window_height = height


@pytest.fixture
def init():
    browser.open(url)
