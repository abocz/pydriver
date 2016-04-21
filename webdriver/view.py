from __future__ import print_function

import inspect

from selenium.common.exceptions import NoSuchElementException

from webdriver.elements import Element


class View(object):
    def __init__(self):
        self.driver = None

    def url(self):
        pass

    def __set_driver__(self, driver):
        self.driver = driver

    def is_loaded(self):
        required_elements = self.get_required_elements()
        for element in required_elements:
            by = element.by
            value = element.value
            try:
                web_element = self.driver.find_element(by, value)
            except NoSuchElementException:
                return False
            element.web_element = web_element
        return True

    def get_element_fields(self):
        return [f for f in inspect.getmembers(self, lambda f:isinstance(f, Element))]

    def get_optional_elements(self):
        return [f[1] for f in self.get_element_fields() if not f[1].required]

    def get_required_elements(self):
        required_fields = [f[1] for f in self.get_element_fields() if f[1].required]
        if len(required_fields) == 0:
            raise Exception('View must have at least one required field.')
        return required_fields

