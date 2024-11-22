from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_CHART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_TEXT = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    BOOK_TEXT_ADDED_TO_CHART = (By.CSS_SELECTOR, "#messages .alertinner strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main p")
    BOOK_PRICE_ADDED_TO_CHART = (By.CSS_SELECTOR, "#messages .alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")
