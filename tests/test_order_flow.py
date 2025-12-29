import pytest
import allure
from data import TestData


class TestOrderFlow:
    
    @allure.title("Заказ черного самоката через верхнюю кнопку - набор данных 1")
    def test_order_black_scooter_via_top_button_data_1(self, main_page, order_page):
        with allure.step("Принять куки"):
            main_page.accept_cookies()
        
        with allure.step("Нажать на верхнюю кнопку 'Заказать'"):
            main_page.click_order_button_top()
        
        with allure.step("Заполнить форму заказа черного самоката"):
            is_successful = order_page.complete_order_with_black_scooter(TestData.ORDER_DATA_1)
        
        with allure.step("Проверить успешное оформление заказа"):
            assert is_successful, "Заказ черного самоката не был успешно оформлен"
    
    @allure.title("Заказ черного самоката через нижнюю кнопку - набор данных 1")
    def test_order_black_scooter_via_bottom_button_data_1(self, main_page, order_page):
        with allure.step("Принять куки"):
            main_page.accept_cookies()
        
        with allure.step("Нажать на нижнюю кнопку 'Заказать'"):
            main_page.click_order_button_bottom()
        
        with allure.step("Заполнить форму заказа черного самоката"):
            is_successful = order_page.complete_order_with_black_scooter(TestData.ORDER_DATA_1)
        
        with allure.step("Проверить успешное оформление заказа"):
            assert is_successful, "Заказ черного самоката не был успешно оформлен"
    
    @allure.title("Заказ серого самоката через верхнюю кнопку - набор данных 1")
    def test_order_grey_scooter_via_top_button_data_1(self, main_page, order_page):
        with allure.step("Принять куки"):
            main_page.accept_cookies()
        
        with allure.step("Нажать на верхнюю кнопку 'Заказать'"):
            main_page.click_order_button_top()
        
        with allure.step("Заполнить форму заказа серого самоката"):
            is_successful = order_page.complete_order_with_grey_scooter(TestData.ORDER_DATA_1)
        
        with allure.step("Проверить успешное оформление заказа"):
            assert is_successful, "Заказ серого самоката не был успешно оформлен"
    
    @allure.title("Заказ серого самоката через нижнюю кнопку - набор данных 1")
    def test_order_grey_scooter_via_bottom_button_data_1(self, main_page, order_page):
        with allure.step("Принять куки"):
            main_page.accept_cookies()
        
        with allure.step("Нажать на нижнюю кнопку 'Заказать'"):
            main_page.click_order_button_bottom()
        
        with allure.step("Заполнить форму заказа серого самоката"):
            is_successful = order_page.complete_order_with_grey_scooter(TestData.ORDER_DATA_1)
        
        with allure.step("Проверить успешное оформление заказа"):
            assert is_successful, "Заказ серого самоката не был успешно оформлен"
    
    @allure.title("Заказ черного самоката через нижнюю кнопку - набор данных 2")
    def test_order_black_scooter_via_bottom_button_data_2(self, main_page, order_page):
        with allure.step("Принять куки"):
            main_page.accept_cookies()
        
        with allure.step("Нажать на нижнюю кнопку 'Заказать'"):
            main_page.click_order_button_bottom()
        
        with allure.step("Заполнить форму заказа черного самоката"):
            is_successful = order_page.complete_order_with_black_scooter(TestData.ORDER_DATA_2)
        
        with allure.step("Проверить успешное оформление заказа"):
            assert is_successful, "Заказ черного самоката не был успешно оформлен"
    
    @allure.title("Заказ серого самоката через нижнюю кнопку - набор данных 2")
    def test_order_grey_scooter_via_bottom_button_data_2(self, main_page, order_page):
        with allure.step("Принять куки"):
            main_page.accept_cookies()
        
        with allure.step("Нажать на нижнюю кнопку 'Заказать'"):
            main_page.click_order_button_bottom()
        
        with allure.step("Заполнить форму заказа серого самоката"):
            is_successful = order_page.complete_order_with_grey_scooter(TestData.ORDER_DATA_2)
        
        with allure.step("Проверить успешное оформление заказа"):
            assert is_successful, "Заказ серого самоката не был успешно оформлен"