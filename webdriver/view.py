from __future__ import print_function

import inspect

from selenium.common.exceptions import NoSuchElementException

from webdriver.elements.element import Element


class View(object):
    def __init__(self):
        self.driver = None

    def __set_driver__(self, driver):
        self.driver = driver

    def is_loaded(self):
        required_fields = self.get_required_fields()
        for field in required_fields:
            by = field[1].by
            value = field[1].value
            try:
                web_element = self.driver.find_element(by, value)
            except NoSuchElementException:
                return False
            field[1].web_element = web_element
        return True

    def get_element_fields(self):
        return [f for f in inspect.getmembers(self, lambda f:isinstance(f, Element))]

    def get_optional_fields(self):
        element_fields = self.get_element_fields()
        return [f for f in element_fields if not f[1].required]

    def get_required_fields(self):
        all_fields = self.get_element_fields()
        required_fields = [f for f in all_fields if f[1].required]
        if len(required_fields) == 0:
            raise Exception('View must have at least one required field.')
        return required_fields

