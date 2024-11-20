import time

from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_product_page(self):
        self.check_url()
        self.should_be_add_to_chart_button()
        self.add_to_chart()

    def check_url(self):
        assert (
            self.browser.current_url
            == "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        ), "Неверный URL адрес"

    def should_be_add_to_chart_button(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_CHART_BUTTON
        ), "Нет кнопки добавить в корзину"

    def add_to_chart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CHART_BUTTON).click()
        self.solve_quiz_and_get_code()
        element = self.browser.find_element(*ProductPageLocators.ADDED_TO_CHART_TEXT)
        pass
        assert element.text == 'red test!!!'
        time.sleep(30000)
