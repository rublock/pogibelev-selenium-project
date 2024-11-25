from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

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

    def register_new_user(self, email, password):
        self.go_to_login_page()
        self.browser.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD1_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD2_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()