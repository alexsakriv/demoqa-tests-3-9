from selene.support.shared import browser


def select(type, value):
    browser.element(f'[name={type}][value={value}]+label').click()
