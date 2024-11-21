import time

from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def run_product_page_tests(self):
        self.get_book_name()
        self.add_to_chart()
        self.check_book_name_added_to_chart()
        self.check_book_price_added_to_chart()

    def add_to_chart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CHART_BUTTON).click()
        self.solve_quiz_and_get_code()

    def get_book_name(self):
        text = self.browser.find_element(*ProductPageLocators.BOOK_TEXT)
        return text.text

    def get_book_price(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text

    def check_book_name_added_to_chart(self):
        """
        Проверка, что текст после добавления в корзину
        содержит то же название книги, что и добавлена.
        """
        text = self.browser.find_element(*ProductPageLocators.BOOK_TEXT_ADDED_TO_CHART)
        assert text.text == self.get_book_name(), 'Название книги не соответствует добавленной в корзину'

    def check_book_price_added_to_chart(self):
        """
        Проверка, что цена после добавления в корзину
        такая, что и в корзине.
        """
        price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_ADDED_TO_CHART)
        assert price.text == self.get_book_price(), 'Цена книги не соответствует добавленной в корзину'