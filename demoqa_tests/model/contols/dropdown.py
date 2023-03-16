from selene.support.shared import browser
from selene import have


def select(input_data, select_data):
    browser.element('#subjectsInput').click().type(input_data)
    browser.all('.subjects-auto-complete__option').element_by(have.exact_text(select_data)).click()