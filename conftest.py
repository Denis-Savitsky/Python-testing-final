from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='Chrome',
                     help='Choose browser: Chrome or Firefox')
    parser.addoption('--language', action='store', default='en',
                     help='Choose language: ru, en, es, etc.')

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "login_guest: mark test to login from main page"
    )


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')

    browser = None
    if browser_name == 'Chrome':

        print("\nstart Chrome browser for test..")

        # language preferences
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'Firefox':

        print("\nstart Firefox browser for test..")

        # language preferences
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:

        raise pytest.UsageError(f"--browser_name should be Chrome or Firefox, while your input is {browser_name}")

    yield browser
    print('\nquit browser...')
    browser.quit()
