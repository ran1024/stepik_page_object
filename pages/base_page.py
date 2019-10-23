from selenium.common.exceptions import NoSuchElementException

class BasePage():
    """
    Базовая страница, от которой будут унаследованы все остальные классы.
    """
    def __init__(self, browser, url, timeout=10):
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
