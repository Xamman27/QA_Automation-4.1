from selene import browser, have, be


browser.config.hold_browser_open = True

browser.open('https://qa.guru/cms/system/login')
browser.element('.login-form input[name=email]').type('qagurubot@gmail.com')
browser.element('.login-form [name=password]').type('qagurupassword').press_enter()

browser.element('.main-header_login').click()
browser.element('.logined-form').should(have.text('QA_GURU_BOT'))