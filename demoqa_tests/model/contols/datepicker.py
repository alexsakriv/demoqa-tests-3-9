from selene.support.shared import browser


def select(date_type, month, year, day):
    browser.element(f'#{date_type}').click()
    browser.element('.react-datepicker__month-select').send_keys(month)
    browser.element('.react-datepicker__year-select').send_keys(year)
    browser.element(f'.react-datepicker__day--0{day}').click()