from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Форма "Для кого самокат"
    NAME_INPUT = (By.XPATH, ".//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    STATION_SELECT = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    STATION_OPTION = (By.XPATH, ".//div[@class='select-search__select']//button")
    PHONE_INPUT = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")
    
    # Форма "Про аренду"
    DATE_INPUT = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    CLIK_BLIK = (By.XPATH, "//div[@class='Order_Header__BZXOb' and text()='Про аренду']")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, ".//div[@class='Dropdown-control']")
    RENTAL_PERIOD_OPTIONS = (By.XPATH, "//div[@class='Dropdown-menu' and @aria-expanded='true']/div[contains(@class, 'Dropdown-option')]")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")
    CONFIRM_ORDER_BUTTON = (By.XPATH, ".//button[text()='Да']")
    
    # Модальное окно успеха
    SUCCESS_MODAL = (By.CLASS_NAME, "Order_Modal__YZ-d3")
    SUCCESS_TITLE = (By.XPATH, ".//div[contains(text(), 'Заказ оформлен')]")