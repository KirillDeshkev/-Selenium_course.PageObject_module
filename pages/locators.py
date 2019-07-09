from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.CSS_SELECTOR, ".btn-group a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators(object):
    pass


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.XPATH, "//button[@value='Register']")


class ProductPageLocators(object):
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(1) strong")
    PRODUCT_PRICE_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-info strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")


class CartPageLocators(object):
    EMPTY_CART_MESSAGE = (By.XPATH, "//p[contains(text(),'Your basket is empty')]")
    PRODUCTS_IN_CART = (By.CSS_SELECTOR, ".basket-items")
