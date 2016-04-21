from __future__ import print_function

from pydriver.webdriver.mixins import Disableable, Clickable


class Element(object):
    def __init__(self, by, value, required=True):
        self.by = by
        self.value = value
        self.required = required
        self.web_element = None

    def __set_driver__(self, driver):
        self.driver = driver

    def tag_name(self):
        return self.web_element.tag_name()

    def classes(self):
        classes = self.web_element.get_attribute('class')
        if classes is None:
            return None
        return classes.split()

    def attribute(self, name):
        return self.web_element.get_attribute(name)

    def css(self, prop):
        return self.web_element.value_of_css_property(prop)

    def is_displayed(self):
        return self.web_element.is_displayed()

    def __str__(self):
        return '{}: [{}, {}, {}]'.format(self.__class__, self.by, self.value, self.required)


class Button(Element, Disableable, Clickable):
    def __init__(self, by, value, required=True):
        super(Button, self).__init__(by, value, required)


class TextInput(Element, Clickable):
    def __init__(self, by, value, required=True):
        super(TextInput, self).__init__(by, value, required)

    def clear_and_type(self, msg):
        self.web_element.clear()
        self.web_element.send_keys(msg)
