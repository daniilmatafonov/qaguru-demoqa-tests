import time

from selene.support.shared import browser

from model.pages.registration_page import RegistrationForm, ModalDialogSubmittingForm

form = RegistrationForm()
result = ModalDialogSubmittingForm()
url = 'https://demoqa.com/automation-practice-form'


def given_opened_practice_form():
   browser.open(url)
   time.sleep(1)