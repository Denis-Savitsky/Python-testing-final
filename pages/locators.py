from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    EMAIL_INPUT = (By.CSS_SELECTOR, "#id_login-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_login-password")
    NEW_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    NEW_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REPEAT_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")

class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p")
    ALERT_PRODUCT_ADDED = (By.CSS_SELECTOR, ".alert-success .alertinner")
    ALERT_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner")

