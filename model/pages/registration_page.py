from selene import command, have
from selene.support.shared import browser

from model.helpers.utils import Months, get_resources
from model.ui_controls.checkbox import select_hobby
from model.ui_controls.datepicker import DatePicker
from model.ui_controls.dropdown import Dropdown
from model.ui_controls.result_table import ResultTable
from model.ui_controls.tags_input import TagsInput


class RegistrationForm:
    def set_first_name(self, value: str):
        browser.element('#firstName').type(value)
        return self

    def set_last_name(self, value: str):
        browser.element('#lastName').type(value)
        return self

    def set_email(self, value: str):
        browser.element('#userEmail').type(value)
        return self

    def set_gender(self, value: str):
        gender = ''
        if value == 'Male':
            gender = '[for=gender-radio-1]'
        elif value == 'Female':
            gender = '[for=gender-radio-2]'
        elif value == 'Other':
            gender = '[for=gender-radio-2]'
        browser.element(gender).click()
        return self

    def set_mobile_number(self, value: str):
        browser.element('#userNumber').type(value)
        return self

    def set_date_of_birth(self, value: str):
        browser.element('#dateOfBirthInput').click()
        DatePicker(browser.element('#dateOfBirth'))\
            .select_year(value[-4:])\
            .select_month(Months[value[3:6]])\
            .select_day(value[:2])
        return self

    def set_subjects(self, values: list):
        for value in values:
            TagsInput(browser.element('#subjectsInput')).add(value)
        return self

    def subjects_should_have(self, values: list):
        TagsInput(browser.element('#subjectsContainer')).element.all('#css-12jo7m5').should(have.text(' '.join(values)))
        return self

    def set_hobbies(self, values: list):
        for value in values:
            select_hobby(value)
        return self

    def set_photo(self, value: str):
        browser.element('#uploadPicture').send_keys(get_resources(f'{value}'))
        return self

    def set_current_address(self, value: str):
        browser.element('#currentAddress').type(value)
        return self

    def set_state(self, value: str):
        Dropdown(browser.element('#state')).select(value)
        return self

    def set_city(self, value: str):
        Dropdown(browser.element('#city')).autocomplete(value)
        return self

    @staticmethod
    def submit():
        browser.element('#submit').perform(command.js.click)


class ModalDialogSubmittingForm:
    def __init__(self):
        self.element = browser.element('.modal-content')
        self.table = ResultTable(self.element.element('.table'))

    def verify_sent_data(self, *values):
        for i in range(len(values)):
            if isinstance(values[i], list):
                value = ', '.join(values[i])
            else:
                value = values[i]
            self.table.path_to_cell(i + 1, column=2).should(have.exact_text(value))
