from Task_2.pages.base_page import BasePage
from Task_2.locators import ElementLocators
from Task_2.data_classes import ChemicalElement, ChemicalElements


class PeriodicTablePage(BasePage):
    locators = ElementLocators()
    elements_list = ChemicalElements()

    def get_chemical_elements(self):
        all_elements = self.find_elements_on_page(self.locators.ALL_ELEMENTS_LOCATOR)
        for element in all_elements:
            element.click()
            number = self.find_element_on_page(self.locators.ATOMIC_NUMBER).text
            weight = self.find_element_on_page(self.locators.ELEMENT_WEIGHT).text
            name = self.find_element_on_page(self.locators.ELEMENT_NAME).text
            single_element = ChemicalElement(atomic=number, weight=weight, name=name)
            self.elements_list.elements.append(single_element)
        return self.elements_list.elements
