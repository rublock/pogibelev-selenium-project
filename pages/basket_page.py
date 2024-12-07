from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        """
        Проверка, что корзина пуста
        """
        assert not self.is_element_present(
            *BasketPageLocators.BASKET_ITEMS
        ), "Корзина не пуста"

    def should_be_empty_basket_text(self):
        """
        Проверка, что корзина пуста
        """
        text = self.browser.find_element(*BasketPageLocators.BASKET_TEXT)
        assert (
            text.text == "Your basket is empty. Continue shopping"
        ), "Корзина не пуста"
