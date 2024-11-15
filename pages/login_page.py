from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.url == 'http://selenium1py.pythonanywhere.com/', 'Неверный URL адрес'

    def should_be_login_form(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_LINK).click()
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Нет формы входа"

    def should_be_register_form(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_LINK).click()
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Нет формы регистрации"
