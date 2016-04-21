import unittest

from selenium.webdriver.common.by import By

from webdriver.elements import Element
from webdriver.exceptions import *


class ExceptionsTest(unittest.TestCase):
    def test_should_raise_pydriver_exception(self):
        with self.assertRaises(PyDriverException):
            ExceptionRaiser.raise_pydriver_exception()

    def test_should_raise_pydriver_elementnotfoundexception(self):
        try:
            ExceptionRaiser.raise_pydriver_element_not_found()
        except PyDriverElementNotFoundException as error:
            self.assertTrue('This is a PyDriverElementNotFoundException.' in error.msg)
            self.assertTrue('[id, foo, True]' in error.msg)


class ExceptionRaiser(object):
    @staticmethod
    def raise_pydriver_exception():
        raise PyDriverException('This is a PyDriverException.')

    @staticmethod
    def raise_pydriver_element_not_found():
        element = Element(By.ID, 'foo')
        raise PyDriverElementNotFoundException(element, 'This is a PyDriverElementNotFoundException.')

