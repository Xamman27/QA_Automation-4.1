from selene.support.shared import browser
from selene import be, have

browser.config.browser_name = 'firefox'
browser.config.hold_browser_open = True
browser.open('https://demoqa.com/automation-practice-form')
browser.element('[id="firstName"]').should(be.blank).type('ivan')
browser.element('[id="lastName"]').should(be.blank).type('ivanov')
browser.element('[id="userEmail"]').should(be.blank).type('ivanov@gmail.com')
browser.element('[for="gender-radio-1"]').should(be.clickable).click()
browser.element('[id="userNumber"]').should(be.blank).type('0123456789')

browser.element('input[id="dateOfBirthInput"]').should(be.clickable).click()
browser.element('select[class="react-datepicker__month-select"]').should(be.clickable).click()
browser.element('option[value="10"]').should(be.clickable).click()
browser.element('select[class="react-datepicker__year-select"]').should(be.clickable).click()
browser.element('option[value="1989"]').should(be.clickable).click()
browser.element('div[class="react-datepicker__day react-datepicker__day--001"]').should(be.clickable).click()

browser.element('[for=hobbies-checkbox-1]').should(be.clickable).click()
browser.element('[id="currentAddress"]').should(be.blank).type('Russia')
# browser.element('[id="submit"]').should(be.clickable).click() #мешает рекламный банер
browser.element('[id="firstName"]').should(be.clickable).click().press_enter()
browser.element('[id="example-modal-sizes-title-lg"]').should(have.text('Thanks for submitting the form'))
