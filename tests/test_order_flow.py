import pytest
import allure
from data import TestData


class TestOrderFlow:
    
    @allure.title("Позитивный сценарий заказа самоката - набор данных 1")
    @pytest.mark.parametrize("order_button", ["top", "bottom"])
    def test_order_flow_data_1(self, main_page, order_page, order_button):
        with allure.step("Принять куки"):
            main_page.accept_cookies()
        
        with allure.step(f"Нажать на кнопку 'Заказать' ({order_button})"):
            if order_button == "top":
                main_page.click_order_button_top()
            else:
                main_page.click_order_button_bottom()
        
        with allure.step("Заполнить форму заказа"):
            is_successful = order_page.complete_order(TestData.ORDER_DATA_1)
        
        with allure.step("Проверить успешное оформление заказа"):
            assert is_successful, "Заказ не был успешно оформлен"
    
    @allure.title("Позитивный сценарий заказа самоката - набор данных 2")
    def test_order_flow_data_2(self, main_page, order_page):
        with allure.step("Принять куки"):
            main_page.accept_cookies()
        
        with allure.step("Нажать на кнопку 'Заказать' (нижняя)"):
            main_page.click_order_button_bottom()
        
        with allure.step("Заполнить форму заказа"):
            is_successful = order_page.complete_order(TestData.ORDER_DATA_2)
        
        with allure.step("Проверить успешное оформление заказа"):
            assert is_successful, "Заказ не был успешно оформлен"