from __future__ import print_function

import unittest

from mock import MagicMock
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from webdriver.driver import Driver
from webdriver.elements import Button
from webdriver.elements import Element


class ElementTest(unittest.TestCase):
    def test_should_init_correctly(self):
        element = Element(By.ID, 'foo')
        self.assertEqual(element.by, By.ID)
        self.assertEqual(element.value, 'foo')
        self.assertTrue(element.required)
        self.assertIsNone(element.web_element)

    def test_should_set_driver(self):
        element = Element(By.ID, 'foo')
        driver = Driver()
        element.__set_driver__(driver)
        self.assertIsNotNone(element.driver)

    def test_should_allow_mixin(self):
        button = Button(By.ID, 'foo')
        button.web_element = WebElement(None, None)
        button.web_element.is_enabled = MagicMock(return_value=True)
        self.assertTrue(button.is_enabled())
