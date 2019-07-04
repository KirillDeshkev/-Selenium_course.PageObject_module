from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def get_product_info(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return name, price

    def should_be_added_to_cart(self, name, price):
        self.should_contain_product_name(name)
        self.should_contain_product_price(price)

    def should_contain_product_name(self, name):
        assert name == self.browser.find_element(
            *ProductPageLocators.MESSAGE_WITH_PRODUCT_NAME).text, "Product name is incorrect in message"

    def should_contain_product_price(self, price):
        assert price == self.browser.find_element(
            *ProductPageLocators.MESSAGE_WITH_PRODUCT_PRICE).text, "Product price is incorrect in message"
