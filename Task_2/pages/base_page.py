class BasePage(object):

    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.driver.implicitly_wait(timeout)
        self.url = url

    def open_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def find_element_on_page(self, locator):
        return self.driver.find_element(*locator)

    def find_elements_on_page(self, locator):
        return self.driver.find_elements(*locator)