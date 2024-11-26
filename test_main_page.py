import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestGuestActionsInMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_url_and_login_register_forms(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_url()
        page.should_be_login_form()
        page.should_be_register_form()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = BasketPage(browser, link)
        page.open()
        page.go_to_basket()
        page.should_be_empty_basket()
