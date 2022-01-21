import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options




def pytest_addoption(parser):
    parser.addoption('--browser_name',action='store', default='chrome', help="Choose browser: chrome or firefox")
    
    parser.addoption('--language', action='store', default="ru",help="Choose browser: Choose launge: es, ru or en")



@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    language = request.config.getoption('language')
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        driver = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield driver
    print("\nquit browser..")
    driver.quit()
