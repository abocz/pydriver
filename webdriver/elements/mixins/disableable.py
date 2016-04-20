from __future__ import print_function


class Disableable(object):
    def __init__(self, web_element):
        self.web_element = web_element

    def is_enabled(self):
        return self.web_element.is_enabled()
