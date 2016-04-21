from __future__ import print_function

import unittest

from pydriver.webdriver import Driver, PyDriverTimeoutException
from pydriver.webdriver.view import View


@unittest.skip('same instance of FF issue')
class DriverTest(unittest.TestCase):
    def test_should_create_new_driver_upon_init(self):
        driver = Driver()
        self.assertIsNotNone(driver.driver)
        driver.close()

    def test_should_open_url(self):
        driver = Driver()
        driver.open('http://www.google.com')
        self.assertEqual(driver.title(), 'Google')
        driver.close()

    def test_should_open_view(self):
        driver = Driver()
        view = AlwaysLoadedView()
        actual = driver.open(view)
        self.assertIsNotNone(view.driver)
        self.assertIsNotNone(actual)
        self.assertTrue(view.is_loaded())
        driver.close()

    def test_should_timeout_if_view_not_loaded(self):
        driver = Driver()
        view = NeverLoadedView()
        with self.assertRaises(PyDriverTimeoutException):
            driver.open(view)
        driver.close()


class AlwaysLoadedView(View):
    def url(self):
        return 'http://www.google.com'

    def is_loaded(self):
        return True


class NeverLoadedView(View):
    def url(self):
        return 'http://www.google.com'

    def is_loaded(self):
        return False


if __name__ == '__main__':
    unittest.main()
