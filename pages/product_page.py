from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_chart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CHART_BUTTON).click()
        self.solve_quiz_and_get_code()

    def get_book_name(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_TEXT).text

    def get_book_price(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text

    def check_book_name_added_to_chart(self, book_name):
        """
        Проверка, что текст после добавления в корзину
        содержит то же название книги, что и добавлена.
        """
        text = self.browser.find_element(*ProductPageLocators.BOOK_TEXT_ADDED_TO_CHART)
        assert (
            text.text == book_name
        ), "Название книги не соответствует добавленной в корзину"

    def check_book_price_added_to_chart(self, book_price):
        """
        Проверка, что цена после добавления в корзину
        такая же, что и в корзине.
        """
        price = self.browser.find_element(
            *ProductPageLocators.BOOK_PRICE_ADDED_TO_CHART
        )
        assert (
            price.text == book_price
        ), "Цена книги не соответствует добавленной в корзину"

    def should_not_be_success_message(self):
        """
        Проверка отсутствия success сообщения
        """
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success сообщение все-таки присутствует"

    def message_should_disappeared(self):
        """
        Проверка, что нет сообщения об успехе после добавления
        товара в корзину
        """
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success сообщение все-таки присутствует после добавления товара корзину"
