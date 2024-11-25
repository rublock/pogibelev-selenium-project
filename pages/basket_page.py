from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        """
        Проверка, что корзина пуста
        """
        text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET)
        assert (
            text.text == "Your basket is empty. Continue shopping"
        ), "Корзина не пуста"

    def should_not_be_empty_basket(self):
        """
        Проверка, что корзина не пуста
        """
        assert self.is_element_present(
            *BasketPageLocators.NOT_EMPTY_BASKET
        ), "Корзина пуста"
