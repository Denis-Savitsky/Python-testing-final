from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_cart(self):
        btn_add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        btn_add_to_cart.click()

    def compare_product_name(self):
        assert self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text == \
               self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text + " has been added to your basket.", \
                "The product name does not align with the name in the alert"

    def compare_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text in \
               self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_PRICE).text, \
               "The product price does not align with the price in the alert"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message has not disappeared, but should have"
