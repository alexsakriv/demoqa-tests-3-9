from demoqa_tests import app
from demoqa_tests.data.user import get_user


def test_submit(open_browser):
    user = get_user()
    app.practice_page.open().register(user).press_submit().assert_registered(user)
