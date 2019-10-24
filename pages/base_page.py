import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from .locators import BasePageLocators


class BasePage():
    """
    Базовая страница, от которой будут унаследованы все остальные классы.
    """
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    
    def open(self):
        self.browser.get(self.url)
    
    def is_element_present(self, locator, data):
        try:
            self.browser.find_element(locator, data)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, locator, data, timeout=4):
        """
        Проверяем, что элемент не появился на странице в течении заданного времени.
        """
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((locator, data))
            )
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, locator, data, timeout=4):
        """
        Проверяем, что элемент исчезает со страницы за заданное время.
        """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((locator, data))
            )
        except TimeoutException:
            return False
        return True

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented."

    def go_to_login_page(self):
        try:
            login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        except NoSuchElementException:
            assert False, "Login link not found in this page."
        else:
            login_link.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs(12 * math.sin(float(x)))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented.")
