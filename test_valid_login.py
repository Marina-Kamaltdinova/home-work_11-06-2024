from selene import browser, have


def test_wrong_password(setup):
    browser.open('')
    browser.element('[name="email"]').type('m.kamaltdinova@ctrl2go.solutions')
    browser.element('[name="password"]').type('неверный пароль').press_enter()
    browser.element('.btn-error').should(have.text('Неверный пароль'))


def test_password(setup):
    browser.open('')
    browser.element('[name="email"]').type('m.kamaltdinova@ctrl2go.solutions').press_enter()
    browser.element('.btn-error').should(have.text('Не заполнено поле Пароль'))


def test_password_1(setup):
    browser.open('')
    browser.element('[name="password"]').type('p3mukyqeXpSBNF5').press_enter()
    browser.element('.btn-error').should(have.text('Не заполнено поле E-Mail'))
