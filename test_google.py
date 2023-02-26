from selene.support.shared import browser
from selene import be, have

browser.config.browser_name = 'firefox'
browser.config.hold_browser_open = True
browser.open('https://google.com')
browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))