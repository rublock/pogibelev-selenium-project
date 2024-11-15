import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="please try: ru, es or fr",
        choices=("ru", "es", "fr"),
    )


@pytest.fixture()
def browser(request):
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture
def language(request):
    return request.config.getoption("--language")
