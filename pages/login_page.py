from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_LINK).click()
        assert (
            self.browser.current_url
            == "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        ), "Неверный URL адрес"

    def should_be_login_form(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_LINK).click()
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Нет формы входа"

    def should_be_register_form(self):
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM).click()
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM
        ), "Нет формы регистрации"
