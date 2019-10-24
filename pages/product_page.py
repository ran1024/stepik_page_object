from .base_page import BasePage
from .locators import ProductPageLocators
#import time


class ProductPage(BasePage):
    """
    Страница товара
    """
    def _get_name_product(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    
    def _get_cost_product(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text

    def should_be_add_product_to_basket(self):
        product_name = self._get_name_product()
        product_cost = self._get_cost_product()
        self.should_be_add_to_basket_button()
        self.add_product_to_basket()
        self.should_be_message_about_added_to_basket(product_name)
        self.should_be_price_item_in_message(product_cost)

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
                                "There is no button to add to the basket."

    def add_product_to_basket(self):
        promo = self.browser.current_url.find("?promo=newYear")
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        if promo > -1:
            self.solve_quiz_and_get_code()

    def should_be_message_about_added_to_basket(self, product_name):
        success_msg = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert success_msg == product_name, \
                                "There is no message that the item was added to the cart."

    def should_be_price_item_in_message(self, product_cost):
        cost_msg = self.browser.find_element(*ProductPageLocators.COST_MESSAGE).text
        assert cost_msg == product_cost, \
                                "The value of the basket is not equal to the price of the item."

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
                                "Success message is present, but should not be."

    def should_be_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
                                "Success message is not disappear after any time."
