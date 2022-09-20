import os
import time

from selene.support.shared import browser
from selene import have, be, query
from selene.support import by


def test_automation_practice_form():
    browser.open('https://demoqa.com/automation-practice-form')

    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('ivanov_ivan@test_mail.com')
    browser.element('[name="gender"][value="Male"]~label').click()
    browser.element('#userNumber').type('9231234567')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').send_keys('January')
    browser.element('.react-datepicker__year-select').send_keys('1980')
    browser.element('.react-datepicker__day.react-datepicker__day--001').click()
    browser.element('#subjectsInput').type('History').press_enter()
    browser.element('#hobbies-checkbox-1~label').click()
    browser.element('#uploadPicture').send_keys(os.getcwd() + '/test_pic.png')
    browser.element('#currentAddress').type('Russia')
    browser.element('#state input').type('NCR').press_enter()
    browser.element('#city input').type('Delhi').press_enter()
    browser.element('#submit').click()

    tbody = browser.element('.modal-body tbody').all('tr')
    tbody.should(
        have.texts('Student Name Ivan Ivanov',
                   'Student Email ivanov_ivan@test_mail.com',
                   'Gender Male',
                   'Mobile 9231234567',
                   'Date of Birth 01 January,1980',
                   'Subjects History',
                   'Hobbies Sports',
                   'Picture test_pic.png',
                   'Address Russia',
                   'State and City NCR Delhi'))


def test_webtables_add():
    browser.open('/webtables')

    browser.element('#addNewRecordButton').click()
    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('ivanov_ivan@test_mail.com')
    browser.element('#age').type('20')
    browser.element('#salary').type('100')
    browser.element('#department').type('IT')
    browser.element('#submit').click()

    table = browser.element('.rt-tr-group:nth-child(4) div').all('div')[:6]
    table.should(have.texts('Ivan', 'Ivanov', '20', 'ivanov_ivan@test_mail.com', '100', 'IT'))


def test_webtables_edit():
    browser.open('/webtables')

    browser.element('#edit-record-2').click()
    browser.element('#firstName').clear().type('Ivan')
    browser.element('#lastName').clear().type('Ivanov')
    browser.element('#userEmail').clear().type('ivanov_ivan@test_mail.com')
    browser.element('#age').clear().type('20')
    browser.element('#salary').clear().type('100')
    browser.element('#department').clear().type('IT')
    browser.element('#submit').click()

    table = browser.element('.rt-tr-group:nth-child(2) div').all('div')[:6]
    table.should(have.texts('Ivan', 'Ivanov', '20', 'ivanov_ivan@test_mail.com', '100', 'IT'))


def test_webtables_remove():
    browser.open('/webtables')
    browser.element('#delete-record-3').click()

    table = browser.element('.rt-tr-group:nth-child(3) div').all('div')[:6]
    table.should(have.no.texts('Kierra', 'Gentry', '29', 'kierra@example.com', '2000', 'Legal'))
