import os
from selene.support.shared import browser
import web_tests


def select(name):
    browser.element('#uploadPicture').set_value(
        os.path.abspath(
            os.path.join(os.path.dirname(web_tests.__file__), f'resources/{name}')
        )
    )