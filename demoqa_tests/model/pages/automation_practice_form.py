from selene.support.shared import browser
from selene import have, command
from demoqa_tests.model.contols import radiobutton, datepicker, dropdown, checkbox
from demoqa_tests.data.user import User
from demoqa_tests.utils import uploadPicture


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


class PracticePage:
    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=3).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def fill_name(self, firstName, lastName):
        browser.element('#firstName').type(firstName)
        browser.element('#lastName').type(lastName)
        return self

    def fill_email(self, userEmail):
        browser.element('#userEmail').type(userEmail)
        return self

    def fill_phone(self, userNumber):
        browser.element('#userNumber').type(userNumber)
        return self

    def fill_address(self, address):
        browser.element('#currentAddress').type(address)
        return self

    def fill_gender(self, radio_button_type, gender_value):
        radiobutton.select(radio_button_type, gender_value)
        return self

    def fill_birthday(self, date_type, month, year, day):
        datepicker.select(date_type, month, year, day)
        return self

    def fill_subject(self, input_subject, select_subject):
        dropdown.select(input_subject, select_subject)
        return self

    def fill_hobby(self, checkbox_type, checkbox_value):
        checkbox.select(checkbox_type, checkbox_value)
        return self

    def fill_picture(self, picture_name):
        uploadPicture.select(picture_name)
        return self

    def fill_state_and_city(self, state, city):
        browser.element('#state').perform(command.js.scroll_into_view).click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(state)).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(city)).perform(command.js.click)
        return self

    def register(self, user: User):
        self.fill_name(user.firstName, user.lastName)
        self.fill_email(user.userEmail)
        self.fill_phone(user.userNumber)
        self.fill_address(user.address)
        self.fill_gender(user.radio_button_type, user.gender_value)
        self.fill_birthday(user.date_type, user.month, user.year, user.day)
        self.fill_subject(user.input_subject, user.select_subject)
        self.fill_hobby(user.checkbox_type, user.checkbox_value)
        self.fill_picture(user.picture_name)
        self.fill_state_and_city(user.state, user.city)
        return self

    def press_submit(self):
        browser.element('#submit').press_enter()
        return self

    def assert_registered(self, user: User):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{user.firstName} {user.lastName}',
                user.userEmail,
                user.gender_value,
                user.userNumber,
                f'{user.day} {user.month},{user.year}',
                user.select_subject,
                user.checkbox_value,
                user.picture_name,
                user.address,
                f'{user.state} {user.city}'
            )
        )