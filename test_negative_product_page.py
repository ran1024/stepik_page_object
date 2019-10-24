# pytest -v -s --tb=line --language=en test_product_page.py
# Проверка добавления товара в корзину.
import pytest
from .pages.product_page import ProductPage


LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_208/'


@pytest.mark.xfail(reason="Сообщение об успехе должно быть всегда!")
def test_guest_can_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()

def test_guest_can_see_success_message(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="Сообщение об успехе должно быть всегда!")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_product_to_basket()
    page.should_be_disappear_success_message()
