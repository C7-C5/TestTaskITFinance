class BasePage(object):

    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.driver.implicitly_wait(timeout)
        self.url = url

    def open_page(self):
        '''
        Method to open any page by url
        :return: nothing
        '''
        self.driver.get(self.url)
        self.driver.maximize_window()

    def find_element_on_page(self, locator):
        '''
        Method to seek a single element on page by locator
        :return: found element
        '''
        return self.driver.find_element(*locator)

    def find_elements_on_page(self, locator):
        '''
        Method to seek multiple elements on page by locator
        :return: found elements
        '''
        return self.driver.find_elements(*locator)