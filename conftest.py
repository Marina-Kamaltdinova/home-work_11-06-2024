from selene import browser
import pytest


@pytest.fixture()
def setup():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://school.qa.guru/cms/system/login'
    yield
    browser.quit()
