import os

from selene import be, by, have, command
from selene.support.shared import browser

firstName = "Daniil"
lastName = "M"
email = "test@mail.ru"
gender = "Male"
mobileNumber = "1234567890"
birthDay = "9"
birthMonth = "06"
birthMonthStr = "9"
birthYear = "1981"
subjects = ["Computer Science", "English"]
hobbies = "Reading"
currentAddress = "Love street"
state = "NCR"
city = "Delhi"


def test_submit_form(init):
    hide_banners()
    browser.element('#firstName').should(be.blank).type(firstName)
    browser.element('#lastName').should(be.blank).type(lastName)
    browser.element('#userEmail').should(be.blank).type(email)
    browser.element(by.text(gender)).click()
    browser.element('#userNumber').should(be.blank).type(mobileNumber)
    browser.element('#dateOfBirthInput').perform(command.js.scroll_into_view).click()
    browser.element('[value="%s"]' % birthYear).click()
    browser.element('[value="6"]').click()
    browser.element('div[aria-label="Choose Saturday, August 1st, %s"]' % birthYear).click()
    browser.element('#subjectsInput').click().send_keys(subjects[0]).press_enter()
    browser.element('#subjectsInput').click().send_keys(subjects[1]).press_enter()
    browser.element(by.text(hobbies)).click()
    browser.element("#uploadPicture").send_keys(os.path.abspath(f'../images/fry.jpeg'))
    browser.element('#currentAddress').should(be.blank).type(currentAddress)
    browser.element('#state input').type(state).press_tab()
    browser.element('#city input').type(city).press_tab()
    browser.element("#submit").click()
    check_table()


def hide_banners():
    # hide banner
    browser.execute_script('document.querySelector("#fixedban").hidden = "true"')
    # hide footer, show submit button
    browser.execute_script('document.querySelector("footer").hidden = "true";')


def check_table():
    tr = browser.elements("table tr")
    tr.element(1).should(have.text(firstName))
    tr.element(1).should(have.text(lastName))
    tr.element(2).should(have.text(email))
    tr.element(3).should(have.text(gender))
    tr.element(4).should(have.text(mobileNumber))
    tr.element(5).should(have.text("1 August,%s" % birthYear))
    tr.element(6).should(have.text(subjects[0]))
    tr.element(6).should(have.text(subjects[1]))
    tr.element(7).should(have.text(hobbies))
    tr.element(8).should(have.text("Picture fry.jpeg"))
    tr.element(9).should(have.text(currentAddress))
    tr.element(10).should(have.text(state))
    tr.element(10).should(have.text(city))
    browser.element("#closeLargeModal").click()