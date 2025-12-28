import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestNavigation:
    
    @allure.title("Проверка перехода на главную страницу через логотип Самоката")
    def test_scooter_logo_navigation(self, main_page, driver):
        with allure.step("Принять куки"):
            main_page.accept_cookies()
        
        with allure.step("Нажать на логотип Самоката"):
            main_page.click_scooter_logo()
        
        with allure.step("Проверить, что открылась главная страница Самоката"):
            WebDriverWait(driver, 10).until(EC.url_to_be("https://qa-scooter.praktikum-services.ru/"))
            assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"
    
    @allure.title("Проверка перехода на Дзен через логотип Яндекса")
    def test_yandex_logo_navigation(self, main_page, driver):
        with allure.step("Принять куки"):
            main_page.accept_cookies()
        
        with allure.step("Запомнить текущее окно"):
            main_window = driver.current_window_handle
        
        with allure.step("Нажать на логотип Яндекса"):
            main_page.click_yandex_logo()
        
        with allure.step("Переключиться на новую вкладку"):
            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
            handles = driver.window_handles
            driver.switch_to.window(handles[1])
        
        with allure.step("Проверить, что открылась страница Дзен"):
            WebDriverWait(driver, 10).until(lambda d: "dzen.ru" in d.current_url or "yandex.ru" in d.current_url)
            assert "dzen.ru" in driver.current_url or "yandex.ru" in driver.current_url
        
        with allure.step("Закрыть вкладку Дзен и вернуться на главную"):
            driver.close()
            driver.switch_to.window(main_window)