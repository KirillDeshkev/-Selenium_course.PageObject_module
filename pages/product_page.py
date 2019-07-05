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
        self.should_be_success_message()
        self.should_contain_product_name(name)
        self.should_contain_product_price(price)

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "There is no success message"

    def should_contain_product_name(self, name):
        message_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGE).text
        assert name == message_name, "Product name is incorrect in message.\nExpected to find '{}', but found '{}'".format(
            name, message_name)

    def should_contain_product_price(self, price):
        message_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE_IN_SUCCESS_MESSAGE).text
        assert price == message_price, "Product price is incorrect in message.\nExpected to find {}, but found{}".format(
            price, message_price)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_from_page(self):
        assert self.is_element_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is still presented, but should be hidden"
