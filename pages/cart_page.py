from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_be_cart_page(self):
        self.should_be_cart_url()

    def should_be_cart_url(self):
        assert 'basket' in self.browser.current_url, "Browser is not on cart page"

    def should_be_empty(self):
        self.should_be_no_products()
        self.should_be_empty_cart_message()

    def should_be_empty_cart_message(self):
        assert self.is_element_present(*CartPageLocators.EMPTY_CART_MESSAGE), "There is no message, that cart is empty"

    def should_be_no_products(self):
        assert self.is_not_element_present(*CartPageLocators.PRODUCTS_IN_CART), "There are products in cart"
