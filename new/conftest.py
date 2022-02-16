import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action ='store', default = "chrome"# None
                    , help ="Choose browser: chrome or firefox")
    parser.addoption('--language', action ='store', default = None, help = 'Language: ru,en,..')


# @pytest.fixture(scope="function")
@pytest.fixture(scope="class")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        # browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
        # browser = webdriver.Firefox()
    # else:
        # raise pytest.UsageError("--browser_name should be chrome or firefox")
        
    # print("\nstart browser for test..")
    # browser = webdriver.Chrome() 
    # browser = webdriver.Firefox()
    yield browser
    print("\nquit browser..")
    browser.quit()