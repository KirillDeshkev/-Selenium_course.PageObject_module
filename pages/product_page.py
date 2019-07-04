from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def get_product_name(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return name

    def get_product_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return price

    def should_be_added_to_cart(self, name, price):
        self.should_contain_product_name(name)
        self.should_contain_product_price(price)

    def should_contain_product_name(self, name):
        message_name = self.browser.find_element(
            *ProductPageLocators.MESSAGE_WITH_PRODUCT_NAME).text
        assert name == message_name, "Product name is incorrect in message.\nExpected to find '{}', but found '{}'".format(
            name, message_name)

    def should_contain_product_price(self, price):
        message_price = self.browser.find_element(
            *ProductPageLocators.MESSAGE_WITH_PRODUCT_PRICE).text
        assert price == message_price, "Product price is incorrect in message.\nExpected to find {}, but found{}".format(
            price, message_price)
