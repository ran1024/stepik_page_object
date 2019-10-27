from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs > span > a")
    BASKET_LINK_INVALID = (By.CSS_SELECTOR, "#basket_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "form#register_form input#id_registration-email")
    REGISTER_PASSW1 = (By.CSS_SELECTOR, "form#register_form input#id_registration-password1")
    REGISTER_PASSW2 = (By.CSS_SELECTOR, "form#register_form input#id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    COST_MESSAGE = (By.CSS_SELECTOR, ".alertinner p strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    PRODUCT_COST = (By.CSS_SELECTOR, "div.product_main > p")


class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, "div#content_inner div.basket-items")
    BASKET_EMPTY = (By.CSS_SELECTOR, "div#content_inner > p")
