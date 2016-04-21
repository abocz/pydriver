from __future__ import print_function

import unittest

from mock import MagicMock
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from webdriver.driver import Driver
from webdriver.elements import Button
from webdriver.view import View


class ViewTest(unittest.TestCase):
    def test_should_init_correctly(self):
        view = MixedRequiredView()
        self.assertIsNone(view.driver)

    def test_should_set_driver(self):
        view = MixedRequiredView()
        self.assertIsNone(view.driver)
        view.__set_driver__(Driver())
        self.assertIsNotNone(view.driver)

    def test_should_get_optional_elements(self):
        view = MixedRequiredView()
        optional_elements = view.get_optional_elements()
        self.assertEqual(len(optional_elements), 1)
        self.assertEqual(optional_elements[0], view.bar)

    def test_should_get_required_elements(self):
        view = MixedRequiredView()
        required_elements = view.get_required_elements()
        self.assertEqual(len(required_elements), 1)
        self.assertEqual(required_elements[0], view.foo)

    def test_should_throw_exception_if_no_required_elements(self):
        view = MixedRequiredView()
        view.foo.required = False
        with self.assertRaises(Exception):
            view.get_required_elements()

    def test_should_not_be_loaded_with_no_elements_present(self):
        view = MixedRequiredView()
        driver = Driver()
        view.__set_driver__(driver)
        self.assertFalse(view.is_loaded())
        driver.close()

    def test_should_be_loaded_with_elements_present(self):
        web_element = WebElement(None, None)
        view = AllRequiredView()
        driver = Driver()
        driver.find_element = MagicMock(return_value=web_element)
        view.__set_driver__(driver)
        self.assertTrue(view.is_loaded())
        driver.close()


class MixedRequiredView(View):
    foo = Button(By.ID, 'foo')
    bar = Button(By.ID, 'bar', False)


class AllRequiredView(View):
    foo = Button(By.ID, 'foo')

