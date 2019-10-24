# pytest -v -s --tb=line --language=en test_product_page.py
# Проверка добавления товара в корзину.
import pytest
from .pages.product_page import ProductPage


LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


@pytest.mark.parametrize(
    'link', [f'{LINK}?promo=offer{n}' if n != 7 else pytest.param(
        f'{LINK}?promo=offer7', marks=pytest.mark.xfail
    ) for n in range(10)]
)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_product_to_basket()


def test_guest_can_add_product_to_basket_with_promo_newyear(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_product_to_basket()


@pytest.mark.login_page
def test_guest_should_see_login_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.login_page
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
