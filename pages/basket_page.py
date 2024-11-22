from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        """
        Проверка, что корзина пуста
        """
        text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET)
        assert (
            text.text == "Your basket is empty. Continue shopping RED"
        ), "Корзина не пуста"
