link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_button_add(browser):
    browser.get(link)
    assert browser.find_element_by_css_selector(".btn-add-to-basket")
