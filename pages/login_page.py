from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, '"login" is not in the url'

    def should_be_login_form(self):
       assert self.is_element_present(*LoginPageLocators.EMAIL_INPUT) and self.is_element_present(*LoginPageLocators.PASSWORD_INPUT), 'log-in form is present'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.NEW_EMAIL_INPUT) and \
               self.is_element_present(*LoginPageLocators.NEW_PASSWORD_INPUT) and \
               self.is_element_present(*LoginPageLocators.REPEAT_PASSWORD_INPUT), 'register form is present'

    def register_new_user(self, email, password):
        email_form = self.browser.find_element(*LoginPageLocators.NEW_EMAIL_INPUT)
        password_form = self.browser.find_element(*LoginPageLocators.NEW_PASSWORD_INPUT)
        repeat_password_form = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD_INPUT)
        email_form.send_keys(email)
        password_form.send_keys(password)
        repeat_password_form.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

