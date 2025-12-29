import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions as EC


class OrderPage(BasePage):
    
    @allure.step("Заполнить первую форму заказа")
    def fill_first_form(self, name, surname, address, station_index, phone):
        self.send_keys_to_input(OrderPageLocators.NAME_INPUT, name)
        self.send_keys_to_input(OrderPageLocators.SURNAME_INPUT, surname)
        self.send_keys_to_input(OrderPageLocators.ADDRESS_INPUT, address)
        
        # Выбор станции метро
        self.click_on_element(OrderPageLocators.STATION_SELECT)
        station_options = self.wait.until(EC.visibility_of_all_elements_located(OrderPageLocators.STATION_OPTION))
        station_options[station_index].click()
        
        self.send_keys_to_input(OrderPageLocators.PHONE_INPUT, phone)
    
    @allure.step("Нажать кнопку 'Далее'")
    def click_next_button(self):
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)
    
    @allure.step("Заполнить вторую форму заказа с черным самокатом")
    def fill_second_form_with_black_scooter(self, date, period_index, comment):
        self._fill_second_form_common(date, period_index, comment)
        self.click_on_element(OrderPageLocators.COLOR_BLACK)
    
    @allure.step("Заполнить вторую форму заказа с серым самокатом")
    def fill_second_form_with_grey_scooter(self, date, period_index, comment):
        self._fill_second_form_common(date, period_index, comment)
        self.click_on_element(OrderPageLocators.COLOR_GREY)
    
    @allure.step("Заполнить общие поля второй формы заказа")
    def _fill_second_form_common(self, date, period_index, comment):
        # Выбор даты
        self.send_keys_to_input(OrderPageLocators.DATE_INPUT, date)
        
        # Выбор срока аренды
        self.click_on_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        period_options = self.wait.until(
            EC.visibility_of_all_elements_located(OrderPageLocators.RENTAL_PERIOD_OPTIONS)
        )
        period_options[period_index].click()
        
        # Комментарий
        self.send_keys_to_input(OrderPageLocators.COMMENT_INPUT, comment)
    
    @allure.step("Нажать кнопку 'Заказать'")
    def click_order_button(self):
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)
    
    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click_on_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)
    
    @allure.step("Проверить успешное оформление заказа")
    def is_order_successful(self):
        try:
            self.wait_for_element(OrderPageLocators.SUCCESS_TITLE, timeout=10)
            return True
        except:
            return False
    
    @allure.step("Заполнить полную форму заказа c черным самокатом")
    def complete_order_with_black_scooter(self, order_data):
        # Первая форма
        self.fill_first_form(
            order_data['name'],
            order_data['surname'],
            order_data['address'],
            order_data['station_index'],
            order_data['phone']
        )
        self.click_next_button()
        
        # Вторая форма
        self.fill_second_form_with_black_scooter(
            order_data['date'],
            order_data['period_index'],
            order_data['comment']
        )
        self.click_order_button()
        self.confirm_order()
        
        return self.is_order_successful()
    
    @allure.step("Заполнить полную форму заказа с серым самокатом")
    def complete_order_with_grey_scooter(self, order_data):
        # Первая форма
        self.fill_first_form(
            order_data['name'],
            order_data['surname'],
            order_data['address'],
            order_data['station_index'],
            order_data['phone']
        )
        self.click_next_button()
        
        # Вторая форма с серым самокатом
        self.fill_second_form_with_grey_scooter(
            order_data['date'],
            order_data['period_index'],
            order_data['comment']
        )
        self.click_order_button()
        self.confirm_order()
        
        return self.is_order_successful()