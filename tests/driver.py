from __future__ import print_function

import unittest
from webdriver.driver import Driver


class DriverTest(unittest.TestCase):
    def test_should_create_new_driver_upon_init(self):
        driver = Driver()
        self.assertIsNotNone(driver.driver)

    def test_should_close_driver(self):
        driver = Driver()
        self.assertIsNotNone(driver.driver)
        driver.close()

    def test_should_open_url(self):
        return
        driver = Driver()
        driver.open('http://www.google.com')
        self.assertEqual(driver.title(), 'Google')


if __name__ == '__main__':
    unittest.main()
