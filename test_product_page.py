# pytest -v -s --tb=line --language=en test_product_page.py
# Проверка добавления товара в корзину.
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
#    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_product_to_basket()
