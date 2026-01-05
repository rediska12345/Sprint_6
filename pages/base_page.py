import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from curl import Urls

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_main_page(self):
        self.driver.get(Urls.MAIN_PAGE)
    
    def open_order_page(self):
        self.driver.get(Urls.ORDER_PAGE)
    
    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.click()

    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)
        
    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step("Подождать и проверить, что атрибут элемента содержит текст")
    def wait_for_attribute(self, locator, attribute, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element_attribute(locator, attribute, value)
        )

    @allure.step("Элемент отсутствует на странице")
    def is_element_not_present(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return False
        except:
            return True

    @allure.step("Переключиться на новую вкладку")
    def switch_to_new_window(self):
        handles = self.driver.window_handles
        if len(handles) > 1:
            self.driver.switch_to.window(handles[1])
        return handles

    @allure.step("Вернуться на предыдущую вкладку")
    def switch_to_previous_window(self, handles):
        if len(handles) > 1:
            self.driver.close()
            self.driver.switch_to.window(handles[0])
 
    @allure.step("Ожидание URL")
    def wait_for_url(self, url, timeout=10):
        def url_checker(driver):
            return url in driver.current_url
        return WebDriverWait(self.driver, timeout).until(url_checker)
    
    def find_element(self, locator, time=10):
        with allure.step(f"Поиск элемента: {locator}"):
            return self._wait_for_element(locator, time, find_multiple=False)

    def find_elements(self, locator, time=10):
        with allure.step(f"Поиск элементов: {locator}"):
            return self._wait_for_element(locator, time, find_multiple=True)
     
    def _wait_for_element(self, locator, time=10, find_multiple=False, visible=False):
        if find_multiple:
            if visible:
                return WebDriverWait(self.driver, time).until(
                    EC.visibility_of_all_elements_located(locator)
                )
            else:
                return WebDriverWait(self.driver, time).until(
                    EC.presence_of_all_elements_located(locator)
                )
        else:
            if visible:
                return WebDriverWait(self.driver, time).until(
                    EC.visibility_of_element_located(locator)
                )
            else:
                return WebDriverWait(self.driver, time).until(
                    EC.presence_of_element_located(locator)
                )