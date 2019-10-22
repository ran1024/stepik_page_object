# pytest -v --tb=line --language=en test_main_page.py
#
link = "http://selenium1py.pythonanywhere.com/"


def go_to_login_page(browser):
    link = browser.find_element_by_css_selector("#login_link")
    link.click()


def test_guest_can_do_to_login_page(browser):
    browser.get(link)
    go_to_login_page(browser)
    