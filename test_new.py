from selene import browser, have

def test_example_1():
    browser.element('').should(have)