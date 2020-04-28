from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def is_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS),\
            "There are items in the basket"



