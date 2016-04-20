from __future__ import print_function


class PyDriverException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class PyDriverElementNotFoundException(PyDriverException):
    def __init__(self, element, msg):
        self.element = element
        self.msg = '{}: {}'.format(self.element, msg)
        super(PyDriverElementNotFoundException, self).__init__(self.msg)
