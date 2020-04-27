from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_cart(self):
        btn_add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        btn_add_to_cart.click()

    def compare_product_name(self):
        assert self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_ADDED).text == \
               self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text + " has been added to your basket.", \
                "The product name does not align with the name in the alert"

    def compare_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text in \
               self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_PRICE).text, \
               "The product price does not align with the price in the alert"
