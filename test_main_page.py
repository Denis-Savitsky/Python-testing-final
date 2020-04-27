from pages.main_page import MainPage
from pages.login_page import LoginPage
import time

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) # инициализируем Page Object, передаем в
    # конструктор экземпляр драйвера и url адрес
    page.open()
    page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_url()
    # login_page.should_be_login_form()
    # login_page.should_be_register_form()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_should_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.should_be_login_form()

def test_guest_should_see_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.should_be_register_form()
