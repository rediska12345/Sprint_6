from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопки "Заказать"
    ORDER_BUTTON_TOP = (By.XPATH, "//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    
    # Вопросы о важном
    QUESTIONS = [
        (By.ID, "accordion__heading-0"),
        (By.ID, "accordion__heading-1"),
        (By.ID, "accordion__heading-2"),
        (By.ID, "accordion__heading-3"),
        (By.ID, "accordion__heading-4"),
        (By.ID, "accordion__heading-5"),
        (By.ID, "accordion__heading-6"),
        (By.ID, "accordion__heading-7")
    ]
    
    # Ответы
    ANSWERS = [
        (By.ID, "accordion__panel-0"),
        (By.ID, "accordion__panel-1"),
        (By.ID, "accordion__panel-2"),
        (By.ID, "accordion__panel-3"),
        (By.ID, "accordion__panel-4"),
        (By.ID, "accordion__panel-5"),
        (By.ID, "accordion__panel-6"),
        (By.ID, "accordion__panel-7")
    ]
    
    # Логотипы
    SCOOTER_LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    YANDEX_LOGO = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")
    
    # Кнопка принятия куки
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")