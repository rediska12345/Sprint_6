import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    
    @allure.step("Принять куки")
    def accept_cookies(self):
        try:
            self.click_on_element(MainPageLocators.COOKIE_BUTTON)
        except:
            pass
    
    @allure.step("Кликнуть на кнопку 'Заказать' вверху")
    def click_order_button_top(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_TOP)
    
    @allure.step("Кликнуть на кнопку 'Заказать' внизу")
    def click_order_button_bottom(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click_on_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
    
    @allure.step("Кликнуть на вопрос")
    def click_question(self, question_index):
        question_locator = MainPageLocators.QUESTIONS[question_index]
        self.scroll_to_element(question_locator)
        self.click_on_element(question_locator)
    
    @allure.step("Получить текст ответа")
    def get_answer_text(self, answer_index):
        answer_locator = MainPageLocators.ANSWERS[answer_index]
        return self.get_text_on_element(answer_locator)
    
    @allure.step("Проверить, что ответ отображается")
    def is_answer_displayed(self, answer_index):
        answer_locator = MainPageLocators.ANSWERS[answer_index]
        return self.wait_for_element(answer_locator).is_displayed()
    
    @allure.step("Кликнуть на логотип Самоката")
    def click_scooter_logo(self):
        self.click_on_element(MainPageLocators.SCOOTER_LOGO)
    
    @allure.step("Кликнуть на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_on_element(MainPageLocators.YANDEX_LOGO)