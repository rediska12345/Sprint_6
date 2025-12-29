import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from curl import Urls

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1200,800")
    options.add_argument("--headless")
    service = Service()
    driver = webdriver.Firefox(service=service, options=options)
    driver.get(Urls.MAIN_PAGE)
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    from pages.main_page import MainPage
    return MainPage(driver)


@pytest.fixture
def order_page(driver):
    from pages.order_page import OrderPage
    return OrderPage(driver)