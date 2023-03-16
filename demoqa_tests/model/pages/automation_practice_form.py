from selene.support.shared import browser
from selene import have, command


def given_opened():
    browser.open('https://demoqa.com/automation-practice-form')


def remove_ads():
    browser.all('[id^=google_ads][id$=container__]').with_(timeout=3).wait_until(
        have.size_greater_than_or_equal(3)
    )
    browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)


def input_info(firstName, lastName, userEmail, userNumber, address):
    browser.element('#firstName').type(firstName)
    browser.element('#lastName').type(lastName)
    browser.element('#userEmail').type(userEmail)
    browser.element('#userNumber').type(userNumber)
    browser.element('#currentAddress').type(address)


def select_state_and_city(state, city):
    browser.element('#state').perform(command.js.scroll_into_view).click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(state)).click()
    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(city)).perform(command.js.click)


def press_submit():
    browser.element('#submit').press_enter()


def then(name, email, gender, number, dateOfBirth, subject, hobby, picture, address, stateAndCity):
    browser.element('.table').all('td').even.should(
        have.exact_texts(
            name,
            email,
            gender,
            number,
            dateOfBirth,
            subject,
            hobby,
            picture,
            address,
            stateAndCity,
        )
    )