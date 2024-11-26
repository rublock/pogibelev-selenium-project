from faker import Faker
import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


@pytest.mark.need_review
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.page = LoginPage(browser, link)
        self.page.open()
        fake = Faker()
        email = fake.email()
        password = fake.password(
            length=10, special_chars=True, digits=True, upper_case=True, lower_case=True
        )
        self.page.register_new_user(email, password)
        self.page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        book_name = page.get_book_name()
        book_price = page.get_book_price()
        page.add_to_chart()
        page.go_to_basket()
        page.check_book_name_added_to_chart(book_name)
        page.check_book_price_added_to_chart(book_price)


@pytest.mark.need_review
class TestGuestActionsInProductPage:
    def test_guest_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        book_name = page.get_book_name()
        book_price = page.get_book_price()
        page.add_to_chart()
        page.go_to_basket()
        page.check_book_name_added_to_chart(book_name)
        page.check_book_price_added_to_chart(book_price)

    @pytest.mark.xfail(reason="Ожидаемая ошибка, корзина должна быть пуста")
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = BasketPage(browser, link)
        page.open()
        page.go_to_basket()
        page.should_be_empty_basket()
        page.should_not_be_empty_basket()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_login_link()
