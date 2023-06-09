import pytest
from selene.support.shared import browser
from selene import command, have


@pytest.fixture(autouse=True)
def open_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    browser.quit()