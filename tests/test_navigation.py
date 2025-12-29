import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from curl import Urls


class TestNavigation:
    
    @allure.title("Проверка перехода на главную страницу через логотип Самоката")
    def test_scooter_logo_navigation(self, driver, main_page):
        with allure.step("Принять куки"):
            main_page.accept_cookies()
        
        with allure.step("Нажать на логотип Самоката"):
            main_page.click_scooter_logo()
        
        with allure.step("Проверить, что открылась главная страница Самоката"):
            main_page.wait.until(lambda d: Urls.MAIN_PAGE in d.current_url)
            assert Urls.MAIN_PAGE in driver.current_url, \
                f"Ожидался URL с {Urls.MAIN_PAGE}, получен: {driver.current_url}"
        
    @allure.title("Проверка перехода на Дзен через логотип Яндекса")
    def test_yandex_logo_navigation(self, driver, main_page):
        with allure.step("Принять куки"):
            main_page.accept_cookies()
     
        with allure.step("Нажать на логотип Яндекса"):
            main_page.click_yandex_logo()
        
        with allure.step("Переключиться на новую вкладку"):
            main_page.switch_to_new_window()
        
        with allure.step("Проверить, что открылась страница Дзен"):
            main_page.wait.until(lambda d: Urls.DZEN_URL in d.current_url or Urls.YANDEX_URL in d.current_url)
            assert Urls.DZEN_URL in driver.current_url or Urls.YANDEX_URL in driver.current_url, \
                f"Ожидался URL с {Urls.DZEN_URL} или {Urls.YANDEX_URL}, получен: {driver.current_url}"