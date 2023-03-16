from selene.support.shared import browser
from selene import have


def select(type, value):
    browser.all(f'[for^={type}-checkbox]').element_by(have.exact_text(value)).click()