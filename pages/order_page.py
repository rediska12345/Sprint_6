import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage(BasePage):
    
    @allure.step("Заполнить первую форму заказа")
    def fill_first_form(self, name, surname, address, station_index, phone):
        self.send_keys_to_input(OrderPageLocators.NAME_INPUT, name)
        self.send_keys_to_input(OrderPageLocators.SURNAME_INPUT, surname)
        self.send_keys_to_input(OrderPageLocators.ADDRESS_INPUT, address)
        
        # Выбор станции метро
        self.click_on_element(OrderPageLocators.STATION_SELECT)
        station_options = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(OrderPageLocators.STATION_OPTION)
        )
        if station_index < len(station_options):
            station_options[station_index].click()
        
        self.send_keys_to_input(OrderPageLocators.PHONE_INPUT, phone)
    
    @allure.step("Нажать кнопку 'Далее'")
    def click_next_button(self):
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)
    
    @allure.step("Заполнить вторую форму заказа")
    def fill_second_form(self, date, period_index, color, comment):
        # Выбор даты
        self.send_keys_to_input(OrderPageLocators.DATE_INPUT, date)
        
        # Выбор срока аренды
        self.click_on_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        period_options = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(OrderPageLocators.RENTAL_PERIOD_OPTIONS))
        if period_index < len(period_options):
            period_options[period_index].click()
        
        # Выбор цвета
        if color == "black":
            self.click_on_element(OrderPageLocators.COLOR_BLACK)
        elif color == "grey":
            self.click_on_element(OrderPageLocators.COLOR_GREY)
        
        # Комментарий
        if comment:
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
    
    @allure.step("Заполнить полную форму заказа")
    def complete_order(self, order_data):
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
        self.fill_second_form(
            order_data['date'],
            order_data['period_index'],
            order_data['color'],
            order_data['comment']
        )
        self.click_order_button()
        self.confirm_order()
        
        return self.is_order_successful()