from selene.support.conditions import have
from selene.support.shared import browser


def select_hobby(hobby: str):
    browser.element('#hobbiesWrapper').all('.custom-checkbox').element_by(have.exact_text(hobby)).click()
