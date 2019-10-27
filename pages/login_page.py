import time
from selenium.common.exceptions import NoSuchElementException

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url.find("login") != -1, "This is not login URL."

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present!"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present!"

    def register_new_user(self, email, password):
        time.sleep(0.2)
        try:
            self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
            self.browser.find_element(*LoginPageLocators.REGISTER_PASSW1).send_keys(password)
            self.browser.find_element(*LoginPageLocators.REGISTER_PASSW2).send_keys(password)
        except NoSuchElementException:
            assert False, "Registration field(s) not found in login page."
        try:
            self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
        except NoSuchElementException:
            assert False, "Registration button not found in login page."
