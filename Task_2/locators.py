from selenium.webdriver.common.by import By

class ElementLocators():

    ALL_ELEMENTS_LOCATOR = (By.CSS_SELECTOR, "li[tabindex='0']")
    ATOMIC_NUMBER = (By.TAG_NAME, 'b')
    ELEMENT_NAME = (By.TAG_NAME, 'em')
    ELEMENT_WEIGHT = (By.TAG_NAME, 'data')