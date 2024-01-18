from selenium import webdriver
from pages.periodic_pable_page import PeriodicTablePage
from urls import MAIN_PAGE_URL


def get_all_elements_list():
    driver = webdriver.Chrome()
    page = PeriodicTablePage(driver=driver, url=MAIN_PAGE_URL)
    page.open_page()
    all_elements = page.get_chemical_elements()
    print(all_elements)

if __name__ == '__main__':
    get_all_elements_list()
