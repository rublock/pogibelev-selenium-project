import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser(request):
    print("\nЗапуск браузера")
    user_language = request.config.getoption("language")
    print(f"Выбранный язык: {user_language}")
    options = Options()
    options.add_experimental_option(
        'prefs', 
        {'intl.accept_languages': user_language}
    )
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nВыход из браузера")
    browser.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Choose browser language"
    )
    
