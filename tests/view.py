from __future__ import print_function

import unittest

from mock import MagicMock
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from webdriver.driver import Driver
from webdriver.elements.button import Button
from webdriver.view import View


class ViewTest(unittest.TestCase):
    def test_should_set_driver(self):
        view = HomePage()
        self.assertIsNone(view.driver)
        view.__set_driver__(Driver())
        self.assertIsNotNone(view.driver)

    def test_should_get_optional_fields(self):
        view = HomePage()
        optional_fields = view.get_optional_fields()
        self.assertEqual(len(optional_fields), 1)
        self.assertEqual(optional_fields[0][1], view.bar)

    def test_should_get_required_fields(self):
        view = HomePage()
        required_fields = view.get_required_fields()
        self.assertEqual(len(required_fields), 1)
        self.assertEqual(required_fields[0][1], view.foo)

    def test_should_throw_exception_if_no_required_fields(self):
        view = HomePage()
        view.foo.required = False
        with self.assertRaises(Exception):
            view.get_required_fields()

    def test_should_not_be_loaded_with_no_elements_present(self):
        view = HomePage()
        driver = Driver()
        view.__set_driver__(driver)
        self.assertFalse(view.is_loaded())

    def test_should_be_loaded_with_elements_present(self):
        web_element = WebElement(None, None)
        view = AllRequiredView()
        driver = Driver()
        driver.find_element = MagicMock(return_value=web_element)
        view.__set_driver__(driver)
        self.assertTrue(view.is_loaded())


class HomePage(View):
    foo = Button(By.ID, 'foo')
    bar = Button(By.ID, 'bar', False)


class AllRequiredView(View):
    foo = Button(By.ID, 'foo')

