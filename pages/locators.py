from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT = (By.NAME, "registration-email")
    PASSWORD1_INPUT = (By.NAME, "registration-password1")
    PASSWORD2_INPUT = (By.NAME, "registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_CHART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_TEXT = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    BOOK_TEXT_ADDED_TO_CHART = (By.XPATH, "//h3/a[contains(text(), 'shellcoder')]")
    BOOK_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main p")
    BOOK_PRICE_ADDED_TO_CHART = (By.XPATH, "//p[contains(text(), '£9.99')]")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")


class BasketPageLocators:
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")
    NOT_EMPTY_BASKET = (By.CSS_SELECTOR, "#basket-items")
