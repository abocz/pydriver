from __future__ import print_function


class Disableable(object):
    def __init__(self, _web_element):
        self._web_element = _web_element

    def is_enabled(self):
        return self._web_element.is_enabled()
