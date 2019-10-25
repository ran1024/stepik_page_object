from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    """
    Страница корзины товаров пользователя.
    """
    def should_be_basket_url(self):
        text = 'basket'
        assert self.browser.current_url.endswith("/basket/"), f"This is not {text} URL."
    
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
                        "Products are present in the basket, but should not be."

    def should_be_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), \
                        "Basket is not empty."
