import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
    )


@pytest.fixture()
def browser(request):
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture
def language(request):
    return request.config.getoption("--language")
